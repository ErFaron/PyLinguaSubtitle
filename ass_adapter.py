import datetime

import ass
import pysrt
from ass.data import Color
from pysrt import SubRipItem
from ass import Document, Style, Dialogue, ScriptInfoSection
import ast
from PIL import ImageFont
from timeit import timeit


def wrap(string, word):
    decorated_word = ("{\\alpha&H00&, \c&H999999&}" + word + "{\\alpha,\c}")
    return string.replace(word, decorated_word)


def convert_time_string_srt_to_ass(string):
    return str(string).replace(",", ".")[:11]


def get_pil_text_size(text, font_size, font_name):
    font = ImageFont.truetype(font_name, font_size)
    size = font.getsize(text)
    return size


def get_str_width(line, font_size):
    font = ImageFont.truetype('arial.ttf', font_size)
    size = font.getsize(line)
    return size[0]


def insert_word_translation(word_translate: str, start: int, text_speech: str):
    translate_margin_h = 300
    script_line = ""
    min_pos = 0
    max_pos = 0
    main_font_size = 48
    translate_font_size = 36
    # margin_v = int(len(lines) * main_font_size + 10 + (len(lines) - 1) * main_font_size / 2)
    # print(margin_v)
    max_pos += len(text_speech)
    if min_pos <= start < max_pos:
        total_width_pixel = get_str_width(text_speech, main_font_size)
        start_pixel = get_str_width(text_speech[0:start - min_pos], main_font_size)
        from_position = start_pixel - total_width_pixel / 2
        translate_width_pixel = get_str_width(word_translate, translate_font_size)
        space_width_pixel = get_str_width(" ", translate_font_size)
        scale_x = 100
        if (from_position + translate_width_pixel + space_width_pixel) > translate_margin_h:
            new_translate_width_pixel = translate_margin_h - from_position
            if new_translate_width_pixel / (translate_width_pixel + space_width_pixel) < 0.6:
                scale_x = 60
            else:
                scale_x = int(new_translate_width_pixel / (translate_width_pixel + space_width_pixel) * 100)
            translate_width_pixel = translate_width_pixel * scale_x / 100
            while len(word_translate) > 2 and (
                    from_position + translate_width_pixel + space_width_pixel * scale_x / 100) > translate_margin_h:
                word_translate = word_translate[0:len(word_translate) - 2]
                word_translate += '…'
                translate_width_pixel = get_str_width(word_translate, translate_font_size) * scale_x / 100
        margin = from_position + translate_width_pixel / 2
        fill_dot_width_pixel = get_str_width(".", translate_font_size) / 4
        fill_dot_count = abs(int(margin * 2.0 / fill_dot_width_pixel))
        fill_dot_left = "." * fill_dot_count if margin > 0 else ""
        fill_dot_right = "." * fill_dot_count if margin <= 0 else ""
        script_line = f'{{\\alpha&HFF&\\fscx25}}{fill_dot_left}{{\\alpha&H00&\\fscx{scale_x}}}{word_translate}{{\\alpha&HFF&\\fscx25}}{fill_dot_right}'
    return script_line


# margin_v = int(margin_v - main_font_size - main_font_size / 2)
# print(margin_v)


class ASSAdapterItem(SubRipItem):
    def __init__(self, sub_item):
        super().__init__(index=sub_item.index, start=sub_item.start, end=sub_item.end, text=sub_item.text,
                         position=sub_item.position)
        self.start_string = convert_time_string_srt_to_ass(sub_item.start)
        self.end_string = convert_time_string_srt_to_ass(sub_item.end)
        self.text_array = str.splitlines(sub_item.text)
        # print(self.main_string_array)
        # self.text_array_format = []
        self.text_translate_array = []
        self.text = str(sub_item.text).replace('\n', "\\N\\N")

    def wrap_word(self, word):
        self.text = wrap(self.text, word)


class ASSAdapter:
    def __init__(self, subs: pysrt.SubRipFile, word_index: dict, dictionary: list, path: str, debug_mode: bool = False):
        self.debug_mode = debug_mode
        self.subs = pysrt.SubRipFile(subs)
        self.word_index = dict(word_index)
        self.dictionary = list(dictionary)
        self.ass_document = Document()
        self.ass_array = []
        self.unknown_stem_indexes = self.get_indexes_by_stems(self.get_unknown_stems())
        for i in self.subs:
            if i.index in self.unknown_stem_indexes:
                # print(i.index)
                self.ass_array.append(ASSAdapterItem(i))
        self.stems_unknown = self.get_unknown_stems()
        for stem in self.stems_unknown:
            self.wrap_words_by_stem(stem)
        self.path = path
        self.create_ass_document()
        self.save_ass_to_file()

    def translate(self, stem: str):
        for i in self.dictionary:
            if i['Stem'] == stem:
                return i['Translate']

    def get_unknown_stems(self):
        stems_unknown = []
        for i in self.dictionary:
            if i['Known'] == 0 and i['Translate'] != '':
                stems_unknown.append(i['Stem'])
        return stems_unknown

    def get_indexes_by_stem(self, stem):
        result = set()
        for i in self.word_index[stem]:
            result.add(i['Srt_item_index'])
        return result

    def wrap_words_by_stem(self, stem):
        if self.translate(stem) != '':
            for i in self.word_index[stem]:
                for ass_item in self.ass_array:
                    if i['Srt_item_index'] == ass_item.index:
                        ass_item.wrap_word(i['Word'])
                        break
            # print((self.ass_array[i['Srt_item_index']]))
            # print(self.ass_array[i['Srt_item_index']])
            # self.ass_array[i['Srt_item_index']].wrap_word(i['Word'])

    def get_indexes_by_stems(self, stem_set):
        result = set()
        for i in stem_set:
            result.update(self.get_indexes_by_stem(i))
        return sorted(result)

    def create_ass_document(self):
        # self.ass_document.info.extend(ScriptType='v4.00+')
        self.ass_document.info = ScriptInfoSection('Script Info', dict(
            [('ScriptType', 'v4.00+'), ('PlayResX', 720), ('PlayResY', 1280)]))
        self.ass_document.styles.extend(
            (Style(name='Default', fontname='Arial', fontsize=48.0, primary_color=Color(r=0x99, g=0x99, b=0x99, a=0x00),
                   secondary_color=Color(r=0xff, g=0xff, b=0xff, a=0x00),
                   outline_color=Color(r=0x00, g=0x00, b=0x00, a=0x00),
                   back_color=Color(r=0x00, g=0x00, b=0x00, a=0xff),
                   bold=False, italic=False, underline=False, strike_out=False, scale_x=100.0, scale_y=100.0,
                   spacing=0.0,
                   angle=0.0, border_style=1, outline=2.0, shadow=2.0, alignment=2, margin_l=0, margin_r=0, margin_v=10,
                   encoding=1)
             ,
             Style(name='Translate', fontname='Arial', fontsize=36.0,
                   primary_color=Color(r=0xcc, g=0xff, b=0xcc, a=0x00),
                   secondary_color=Color(r=0xff, g=0xff, b=0xff, a=0x00),
                   outline_color=Color(r=0x00, g=0x00, b=0x00, a=0x00),
                   back_color=Color(r=0x00, g=0x00, b=0x00, a=0xff),
                   bold=False, italic=False, underline=False,
                   strike_out=False, scale_x=100.0, scale_y=100.0, spacing=0.0, angle=0.0, border_style=1, outline=2.0,
                   shadow=2.0, alignment=2, margin_l=0, margin_r=0, margin_v=10, encoding=1)))
        for i in self.ass_array:
            self.ass_document.events.append(
                Dialogue(layer=0, start=i.start_string, end=i.end_string, style='Default', name='NTP',
                         margin_l=0, margin_r=0, margin_v=0, effect='!Effect',
                         text=i.text))
            if len(i.text_array) == 1:
                margin_v_by_string = {0: 52}
            else:
                margin_v_by_string = {0: 124, 1: 52}
            for j, string in enumerate(i.text_array):
                layer = 0
                for stem in self.stems_unknown:
                    for word in self.word_index[stem]:
                        if word['Srt_item_index'] == i.index and j == word['Srt_item_line_number']:
                            for pos in word['Srt_item_word_positions']:
                                if self.debug_mode:
                                    print()
                                    print(f'{i.start}')
                                    print(f'{i.text}')
                                    print(f'[{j}] {string}')
                                    print(f'{stem} - {self.translate(stem)}')
                                text = insert_word_translation(self.translate(stem), pos, string)
                                layer += 1
                                self.ass_document.events.append(
                                    Dialogue(layer=layer, start=i.start_string, end=i.end_string,
                                             style='Translate', name='NTP',
                                             margin_l=0, margin_r=0, margin_v=margin_v_by_string[j],
                                             effect='!Effect',
                                             text=text))
                        break

    def save_ass_to_file(self):
        new_path = self.path.replace('.srt', '.ass')
        if self.debug_mode:
            print(new_path)
        with open(new_path, "w", encoding='utf_8_sig') as f:
            self.ass_document.dump_file(f)


if __name__ == '__main__':
    path = 'GUI/Carter.srt'
    subs = pysrt.open(path)
    with open('GUI/dictionary.txt', 'r', encoding='UTF-8') as f:
        dictionary = ast.literal_eval(f.read())
    with open('GUI/word_index.txt', 'r', encoding='UTF-8') as f:
        word_index = ast.literal_eval(f.read())
    ASSAdapter(subs, word_index, dictionary, path, debug_mode=False)
    print("done")
