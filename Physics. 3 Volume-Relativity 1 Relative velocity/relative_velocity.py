from manimae import *

class Galileo(Scene):
    def construct(self):
        galileo_png = ImageMobject('galieo.png').scale(0.5).move_to((-4, 0, 0))
        g_Rel_head = Text('Galilean Relativity', font_size=50, color=GREEN).move_to((3, 3, 0))
        g_Rel_head_underline = Underline(g_Rel_head, color=GREEN)
        g_EN_speech = Text(
            '"...The laws of Physics are \n the same in all inertial \n frames of reference..."',
            color='#ffeca1'
        ).next_to((-1, 1, 0))
        g_TH_speech = Text(
            '"...กฎของฟิสิกส์จะเหมือนกันในทุกกรอบ \n อ้างอิงเฉื่อย..."',
            font='TH Sarabun New', color='#ffeca1'
        ).next_to((-1, -1, 0))
        cc = Text(
            'ใน ค.ศ. 1632 กาลิเลโอได้นำเสนอ "หลักความไม่เปลี่ยนแปลงของกาลิเลโอ"',
            font='TH Sarabun New', font_size=35, t2c={
                '"หลักความไม่เปลี่ยนแปลงของกาลิเลโอ"':GREEN
            }
        ).move_to((0, -3, 0))
        self.play(
            FadeIn(galileo_png),
            Write(g_Rel_head), Write(g_Rel_head_underline), Write(g_EN_speech), Write(g_TH_speech),
            Write(cc)
        )
        self.wait(4)

        cc2 = Text(
            'หรือที่รู้จักกันในชื่อ "ทฤษฎีสัมพัทธภาพคลาสสิกของกาลิเลโอ"', font='TH Sarabun New', font_size=35,
            t2c={'"ทฤษฎีสัมพัทธภาพคลาสสิกของกาลิเลโอ"':GREEN}
        ).move_to((0, -3, 0))
        self.replace(cc, cc2)
        self.wait(4)

        cc3 = MultiText(
            Text('โดยเขาได้นำเสนอหลักการที่ว่า', font='TH Sarabun New', font_size=35),
            Text(
                '"กฎของฟิสิกส์จะเหมือนกันในทุกกรอบอ้างอิงเฉื่อย"', font='TH Sarabun New', font_size=35,
                color='#ffeca1'
            ),
            direction=DOWN
        ).move_to((0, -3, 0))
        self.replace(cc2, cc3)
        self.play(Indicate(g_TH_speech))
        self.wait(4)

        ship_svg = SVGMobject('ship.svg').set_fill(BLUE, opacity=1).next_to((0, 1, 0), UP)
        male_svg = SVGMobject('male.svg').set_fill(YELLOW, opacity=1).scale(0.2).move_to((0, 1.5, 0))
        water = Polygon(
            (-6, 1, 0), (6, 1, 0), (6, 0, 0), (-6, 0, 0)
        ).set_fill([PURPLE, BLUE], opacity=1).set_stroke(opacity=0)
        cc4 = MultiText(
            Text('กาลิเลโอได้ยกตัวอย่างเหตุการณ์', font='TH Sarabun New', font_size=35),
            Text(
                'หากเรือกำลังแล่นด้วยความเร็วคงที่ บนทะเลที่สงบเงียบ และไม่มีการโยกของเรือ',
                font='TH Sarabun New', font_size=35, color=RED
            ),
            direction=DOWN
        ).move_to((0, -3, 0))
        stable_motion = Text('ความเร็วคงที่', font='TH Sarabun New', color=RED).next_to((-5, -1, 0))
        no_wave = Text('ไม่มีคลื่น', font='TH Sarabun New', color=RED).next_to((-5, -2, 0))
        no_shake = Text('ไม่โยก', font='TH Sarabun New', color=RED).next_to((0, -1, 0))
        self.replace(cc3, cc4)
        self.play(
            FadeOut(galileo_png), Unwrite(g_Rel_head), Unwrite(g_Rel_head_underline),
            Unwrite(g_EN_speech), Unwrite(g_TH_speech), FadeIn(ship_svg), FadeIn(water),
            FadeIn(male_svg)
        )
        self.play(Write(stable_motion), Write(no_wave), Write(no_shake))
        self.wait(3)

        cc5 = MultiText(
            Text('ผู้สังเกตที่อยู่ใต้ดาดฟ้าเรือจะไม่สามารถบอกได้เลยว่า', font='TH Sarabun New', font_size=35),
            Text('เรือกำลังเคลื่อนที่หรือหยุดนิ่ง', font='TH Sarabun New', font_size=35),
            direction=DOWN
        ).move_to((0, -3, 0))
        self.replace(cc4, cc5)
        self.play(Indicate(male_svg))
        self.play(
            ship_svg.animate.shift(LEFT*5), male_svg.animate.shift(LEFT*5),
            rate_func=rate_functions.linear, run_time=1
        )
        self.play(
            ship_svg.animate.shift(RIGHT*10), male_svg.animate.shift(RIGHT*10),
            rate_func=rate_functions.linear, run_time=2
        )
        self.play(
            ship_svg.animate.shift(LEFT*5), male_svg.animate.shift(LEFT*5),
            rate_func=rate_functions.linear, run_time=1
        )
        self.wait(3)
        self.play(Indicate(male_svg))
        self.wait()

        cc6 = Text('ผมจะยกอีกตัวอย่างนะครับ', font='TH Sarabun New', font_size=35).move_to((0, -3, 0))
        self.replace(cc5, cc6)
        self.play(
            FadeOut(ship_svg), Unwrite(stable_motion), Unwrite(no_wave), Unwrite(no_shake), FadeOut(water)
        )

        room = Square(side_length=3).set_fill(opacity=0).set_stroke('#ffeca1', opacity=1)
        apple_svg = SVGMobject('apple.svg').scale(0.125).set_fill(RED, opacity=1)
        cc7 = Text('ถ้าเราอยู่ในรถไฟตู้ทึบที่อยู่นิ่ง เรามีแอปเปิลลูกหนึ่ง', font='TH Sarabun New', font_size=35).move_to((0, -3, 0))
        self.replace(cc6, cc7)
        self.play(
            Write(room), male_svg.animate.scale(4).next_to((1, -1.5, 0), UP), FadeIn(apple_svg)
        )
        self.wait(3)

        cc8 = Text('เราปล่อยแอปเปิลตกพื้น แบบนี้ถูกต้องนะครับ', font='TH Sarabun New', font_size=35).move_to((0, -3, 0))
        self.replace(cc7, cc8)
        self.play(apple_svg.animate.move_to((0, -1.5, 0)), rate_func=rate_functions.ease_in_back, run_time=1.5)
        self.wait(3)

        cc9 = MultiText(
            Text('แต่เมื่อรถไฟเคลื่อนที่ด้วยความเร็วคงที่ใดๆ', font='TH Sarabun New', font_size=35),
            Text('แอปเปิลจะยังตกที่พื้นรถไฟจุดเดิมอยู่', font='TH Sarabun New', font_size=35),
            direction=DOWN
        ).move_to((0, -3, 0))
        self.replace(cc8, cc9)
        self.play(
            room.animate.shift(RIGHT*5), male_svg.animate.shift(RIGHT*5),
            apple_svg.animate.move_to((5, 0, 0))
        )
        self.wait()
        self.play(
            room.animate.shift(LEFT*5),
            male_svg.animate.shift(LEFT*5),
            apple_svg.animate.move_to((0, -1.5, 0)),
            rate_func=rate_functions.linear,
            run_time=3
        )
        self.wait(2)

        cc10 = Text(
            'นั้นหมายถึง คนบนรถไฟจะไม่สามารถแยกได้เลยว่าตัวเองเคลื่อนที่อยู่หรือเปล่า', font='TH Sarabun New',
            font_size=35
        ).move_to((0, -3, 0))
        self.replace(cc9, cc10)
        self.wait(4)

        cc11 = Text('นั้นล่ะครับ คือความเฉื่อย', font='TH Sarabun New', font_size=75, color='#ffeca1')
        self.play(
            Unwrite(room), FadeOut(apple_svg), FadeOut(male_svg),
            Transform(cc10, cc11), run_time=2
        )
        self.wait(3)

        self.play(Unwrite(cc10))

        relvel_head = Text('ความเร็วสัมพัทธ์', font='TH Sarabun New', font_size=75, color=BLUE).move_to((0, 3, 0))
        relvel_head_underline = Underline(relvel_head, color=BLUE)
        formu = MathTex(
            r'v_{', r'A', r'B', r'}=v_', r'A', r'-v_', r'B', font_size=50
        )
        formu[1].set_color(GREEN)
        formu[4].set_color(GREEN)
        formu[2].set_color(RED)
        formu[6].set_color(RED)
        cc = Text('หลักการของกาลิเลโอได้ถูกนำไปต่อยอดเป็นแนวคิดความเร็วสัมพัทธ์', font='TH Sarabun New', font_size=35).move_to((0, -3, 0))
        self.play(Write(cc))
        self.play(
            Write(relvel_head), Write(relvel_head_underline), Write(formu)
        )
        self.wait(4)

        cc2 = Text(
                'ความหมายว่า ความเร็วของวัตถุหนึ่งเมื่อเทียบกับความเร็วของอีกวัตถุหนึ่ง ในกรอบอ้างอิงเฉื่อย',
                font='TH Sarabun New', font_size=35, t2c={
                    'ความเร็วของวัตถุหนึ่ง':GREEN, 'ความเร็วของอีกวัตถุหนึ่ง':RED
                }
        ).move_to((0, -3, 0))
        self.replace(cc, cc2)
        self.wait(5)

        cc_1 = Text('โดยมีรูปแบบว่า', font='TH Sarabun New', font_size=35)
        cc_2 = MathTex(r'v_{', r'A', r'B', r'}=v_', r'A', r'-v_', r'B', font_size=35).next_to(cc_1)
        cc_2[1].set_color(GREEN)
        cc_2[4].set_color(GREEN)
        cc_2[2].set_color(RED)
        cc_2[6].set_color(RED)
        cc3 = VGroup(cc_1, cc_2).move_to((0, -3, 0))
        self.replace(cc2, cc3)
        self.play(Indicate(formu))
        self.wait(4)

        cc4 = Text(
            'ตัวอย่างนะครับ', font='TH Sarabun New', font_size=35
        ).move_to((0, -3, 0))
        self.replace(cc3, cc4)
        self.play(formu.animate.next_to(relvel_head_underline, DOWN))
        self.wait(3)

        car_A = SVGMobject('car.svg').set_fill(GREEN, opacity=1).scale(0.5).move_to((-5.5, 0.5, 0))
        car_B = SVGMobject('car.svg').set_fill(RED, opacity=1).scale(0.5).move_to((-5.5, -1.5, 0))
        cc5 = Text(
            'เรามีรถเขียวกับรถแดง', font='TH Sarabun New', font_size=35, t2c={
                'รถเขียว':GREEN, 'รถแดง':RED
            }
        ).move_to((0, -3, 0))
        self.replace(cc4, cc5)
        self.play(
            FadeIn(car_A), FadeIn(car_B)
        )
        self.wait(3)

        cc6 = MultiText(
            Text(
                'โดยรถเขียวเคลื่อนที่ด้วยความเร็วคงที่ 100 กม./ชม.', font='TH Sarabun New',
                font_size=35, t2c={'รถเขียว':GREEN, '100 กม./ชม.':GREEN}
            ),
            Text(
                'และรถแดงเคลื่อนที่ด้วยความเร็วคงที่ 180 กม./ชม.', font='TH Sarabun New',
                font_size=35, t2c={'รถแดง':RED, '180 กม./ชม':RED}
            ),
            direction=DOWN
        ).move_to((0, -3, 0))
        self.replace(cc5, cc6)
        self.play(
            car_A.animate.shift(RIGHT*5),
            car_B.animate.shift(RIGHT*9), rate_func=rate_functions.linear, run_time=3,
        )
        self.wait()

        self.play(car_A.animate.move_to((0, 0.5, 0)), car_B.animate.move_to((0, -1.5, 0)))
        cc7 = Text(
            'สำหรับ "ผู้สังเกตบนรถสีเขียว" จะเห็นรถสีแดงเคลื่อนที่แซงไปด้วยความเร็ว 80 กม./ชม.',
            font='TH Sarabun New', font_size=35, t2c={'"ผู้สังเกตบนรถสีเขียว"':GREEN}
        ).move_to((0, -3, 0))
        self.replace(cc6, cc7)
        self.play(car_B.animate.shift(RIGHT*4), rate_func=rate_functions.linear, run_time=3)
        self.wait()

        self.play(car_A.animate.move_to((0, 0.5, 0)), car_B.animate.move_to((0, -1.5, 0)))
        cc8 = Text(
            'ส่วน "ผู้สังเกตบนรถสีแดง" จะเห็นรถสีเขียวเคลื่อนที่ถอยหลังด้วยความเร็ว 80 กม./ชม.',
            font='TH Sarabun New', font_size=35, t2c={'"ผู้สังเกตบนรถสีแดง"':RED}
        ).move_to((0, -3, 0))
        self.replace(cc7, cc8)
        self.play(car_A.animate.shift(LEFT*4), rate_func=rate_functions.linear, run_time=3)
        self.wait()

        cc9 = MultiText(
            Text('ต่อไปจะยกตัวอย่างสถานการร์ที่รถวิ่งสวนกัน', font='TH Sarabun New',font_size=35),
            Text(
                'เรามีรถเขียวกับรถม่วงที่วิ่งสวนกัน', font='TH Sarabun New', font_size=35,
                t2c={'รถเขียว':GREEN, 'รถม่วง':PURPLE}
            ),
            direction=DOWN
        ).move_to((0, -3, 0))
        car_C = SVGMobject('car.svg').set_fill(PURPLE, opacity=1).scale([-0.5, 0.5, 0.5]).move_to((5.5, -1.5, 0))
        self.replace(cc8, cc9)
        self.play(
            car_A.animate.move_to((-5.5, 0.5, 0)), FadeOut(car_B), FadeIn(car_C)
        )
        self.wait(4)

        cc10 = Text(
            'แต่ละคันต่างวิ่งด้วยความเร็ว 100 กม./ชม.', font='TH Sarabun New', font_size=35
        ).move_to((0, -3, 0))
        self.replace(cc9, cc10)
        self.play(
            car_A.animate.shift(RIGHT*5.5),
            car_C.animate.shift(LEFT*5.5), rate_func=rate_functions.linear, run_time=3
        )
        self.wait()

        cc11 = Text(
            'แต่ละคันจะเห็นอีกคันเคลื่อนที่สวนมาด้วยความเร็ว 200 กม./ชม.',
            font='TH Sarabun New', font_size=35
        ).move_to((0, -3, 0))
        self.play(car_A.animate.move_to((-5.5, 0.5, 0)), car_C.animate.move_to((5.5, -1.5, 0)))
        self.replace(cc10, cc11)
        self.play(
            car_C.animate.move_to((car_A.get_x(), -1.5, 0)), rate_func=rate_functions.linear, run_time=3
        )
        self.wait(2)
        self.play(car_C.animate.move_to((5.5, -1.5, 0)))
        self.play(
            car_A.animate.move_to((car_C.get_x(), 0.5, 0)), rate_func=rate_functions.linear, run_time=3
        )
        self.wait(2)

        cc12 = Text(
            'แนวคิดนี้ไม่ได้เพียงบอกแค่ว่า ความเร็วของวัตถุสองวัตถุมาเปรียบเทียบกัน',
            font='TH Sarabun New', font_size=35
        ).move_to((0, -3, 0))
        self.replace(cc11, cc12)
        self.wait(4)

        cc13 = Text(
            'มันยังบอกเราอีกว่า "ไม่มีสิ่งใดที่หยุดเคลื่อนที่สัมบูรณ์อย่างแท้จริง" ทุกสิ่งกำลังเคลื่อนที่อยู่',
            font='TH Sarabun New', font_size=35, t2c={'"ไม่มีสิ่งใดที่หยุดเคลื่อนที่สัมบูรณ์อย่างแท้จริง"':RED}
        ).move_to((0, -3, 0))
        self.replace(cc12, cc13)
        self.wait(4)

        earth_svg = SVGMobject('earth.svg').set_fill(BLUE, opacity=1)
        male_svg = SVGMobject('male.svg').set_fill(GREEN, opacity=1).next_to(earth_svg, UP)
        cc14 = Text(
            'ถึงเราอยู่นิ่งๆ บนโลก', font='TH Sarabun New', font_size=35
        ).move_to((0, -3, 0))
        self.replace(cc13, cc14)
        self.play(
            Unwrite(relvel_head), Unwrite(relvel_head_underline), Unwrite(formu),
            FadeOut(car_A), FadeOut(car_C), FadeIn(earth_svg), FadeIn(male_svg)
        )
        self.wait(3)

        sun_svg = SVGMobject('sun.svg').set_fill(ORANGE, opacity=1)
        cc15 = Text('โลกก็ยังโคจรรอบดวงอาทิตย์', font='TH Sarabun New', font_size=35).move_to((0, -3, 0))
        self.replace(cc14, cc15)
        self.play(
            FadeIn(sun_svg), earth_svg.animate.shift(RIGHT*3).scale(0.25),
            male_svg.animate.move_to((3, 0, 0)).scale(0)
        )
        path = Circle(radius=3)
        self.play(MoveAlongPath(earth_svg, path), run_time=3)
        self.wait()

        galaxy_svg = SVGMobject('galaxy.svg').set_fill(RED, opacity=1)
        cc16 = Text('ดวงอาทิตย์ก็โคจรรอบกาแล็กซี่', font='TH Sarabun New', font_size=35).move_to((0, -3, 0))
        self.replace(cc15, cc16)
        self.play(
            FadeOut(male_svg), FadeOut(earth_svg), FadeIn(galaxy_svg), sun_svg.animate.move_to((3, 0, 0)).scale(0.25)
        )
        self.play(MoveAlongPath(sun_svg, path), run_time=3)
        self.wait()

        cc17 = Text('และกาแล็กซี่ก็ลอยไปลอยมาในอวกาศ', font='TH Sarabun New', font_size=35).move_to((0, -3, 0))
        self.replace(cc16, cc17)
        self.play(FadeOut(sun_svg))
        self.wait(3)

        cc18 = MultiText(
            Text('ฟังดูง่ายใช่ไหมครับเรื่องทฤษฎีสัมพัทธภาพ', font="TH Sarabun New", t2c={'ความเร็วสัมพัทธ์':BLUE}),
            Text('แต่ของจริงมันอยู่ต่อจากนี้ต่างหาก', font='TH Sarabun New', color=RED_D, font_size=75),
            direction=DOWN
        )
        self.play(FadeOut(galaxy_svg), Transform(cc17, cc18))
        self.wait(4)

        self.play(Unwrite(cc17))
