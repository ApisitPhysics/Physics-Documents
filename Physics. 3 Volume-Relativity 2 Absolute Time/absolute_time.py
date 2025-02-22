from manimae import *

class AbsTime(Scene):
    def construct(self):
        poem1 = Text(
            '๏คำเล่าผ่านโบราณสานเอาไว้', font='TH Sarabun New', font_size=75, color='#ffeca1', slant=ITALIC,
            t2c={'โบราณ':BLUE}
        )
        poem2 = Text(
            'เวลาไซร้สัมบูรณ์ภพรังสรรค์', font='TH Sarabun New', font_size=75, color='#ffeca1', slant=ITALIC,
            t2c={'เวลา':GOLD, 'สัมบูรณ์':RED}
        ).next_to(poem1, DOWN)
        poem3 = Text(
            'ไกลแค่ไหนเวลาเราจะเท่ากัน', font='TH Sarabun New', font_size=75, color='#ffeca1', slant=ITALIC,
            t2c={'เวลาเราจะเท่ากัน':BLUE}
        ).next_to(poem2, DOWN)
        poem4 = Text(
            'ทุกคืนวันกลางแสงจันทร์นิรันดร์เอย๚ะ๛', font='TH Sarabun New', font_size=75, color='#ffeca1', slant=ITALIC,
            t2c={'แสง':RED}
        ).next_to(poem3, DOWN)
        poemg = VGroup(poem1, poem2, poem3, poem4).move_to(ORIGIN)
        self.play(Write(poemg[0]), run_time=2)
        self.play(Write(poemg[1]), run_time=2)
        self.play(Write(poemg[2]), run_time=2)
        self.play(Write(poemg[3]), run_time=2)
        self.wait(3)
        self.play(*[FadeOut(obj) for obj in self.mobjects])

        newton_png = ImageMobject('newton.png').scale(3).move_to((-4, 0, 0))
        n_time_head = Text('Philosophiæ Naturalis Principia Mathematica', font_size=50, color=BLUE).next_to((0, 4, 0), DOWN)
        n_time_head_underline = Underline(n_time_head, color=BLUE)
        cc1 = Text('ไอแซค นิวตัน บอกเราว่า เวลาเป็นสิ่งสัมบูรณ์', font='TH Sarabun New', font_size=35).move_to((0, -3, 0))
        self.play(FadeIn(newton_png), Write(n_time_head), Write(n_time_head_underline), Write(cc1))

        n_speech = Text(
            '''
                "Absolute, true, and mathematical time, \n
                of itself, and from its own nature, \n
                flows equably without relation to \n
                anything external, and by another name \n
                is called duration; relative, apparent, \n
                and common time is some sensible and \n
                external measure of duration by the \n
                means of motion, whether accurate or \n
                unequal, which is commonly used instead \n
                of true time."
            ''',
            font_size=20, color=GRAY, slant=ITALIC, t2c={
                'Absolute':'#ffeca1', 'time':'#ffeca1', 'flows equably without relation':'#ffeca1'
            }
        ).next_to(ORIGIN)
        self.play(Write(n_speech), run_time=2)
        self.wait()

        cc2 = Text('เวลาไม่เหมือนความเร็ว เวลาไม่สัมพัทธ์กับอะไรทั้งสิ้น', font='TH Sarabun New', font_size=35).move_to((0, -3, 0))
        self.replace(cc1, cc2)
        self.wait(4)

        self.play(FadeOut(newton_png), Unwrite(n_time_head), Unwrite(n_time_head_underline), Unwrite(n_speech))
        universe_svg = SVGMobject('universe.svg').set_fill(PURPLE, opacity=1)
        clock_svg = SVGMobject('clock.svg').set_fill(GOLD, opacity=1)
        cc3 = Text('เวลาแยกเป็นเอกเทศน์ต่อทุกสิ่งในเอกภพ', font='TH Sarabun New', font_size=35).move_to((0, -3, 0))
        self.replace(cc2, cc3)
        self.play(FadeIn(universe_svg), FadeIn(clock_svg))
        self.play(universe_svg.animate.shift(LEFT*3), clock_svg.animate.shift(RIGHT*3))
        self.wait(3)

        cc4 = Text('ไม่เวลาเกิดอะไรขึ้นในจักรวาล เวลายังคงเดินหน้าต่อไป', font='TH Sarabun New', font_size=35).move_to((0, -3, 0))
        self.replace(cc3, cc4)
        self.play(Indicate(universe_svg))
        self.wait(3)

        cc5 = Text('สมดังคำกล่าวที่ว่า "เวลาไม่เคยรอใคร"', font='TH Sarabun New', font_size=35).move_to((0, -3, 0))
        self.replace(cc4, cc5)
        self.wait(3)

        cc6 = Text('ไม่ว่าเราอยู่ตรงไหนในจักรวาล เราจะเห็นเวลาเท่ากันเสมอ', font='TH Sarabun New', font_size=35).move_to((0, -3, 0))
        self.replace(cc5, cc6)
        male1 = SVGMobject('male.svg').set_fill(BLUE, opacity=1).next_to((-4, 0, 0), UP)
        male2 = SVGMobject('male.svg').set_fill(GREEN, opacity=1).next_to((4, 0, 0), UP)
        self.play(FadeOut(universe_svg), FadeOut(clock_svg), FadeIn(male1), FadeIn(male2))
        time1 = Text('ตรงนี้บ่ายสาม', font='TH Sarabun New', font_size=25).move_to(male1).set_opacity(0)
        time2 = Text('ตรงนี้ก็บ่ายสาม', font='TH Sarabun New', font_size=25).move_to(male2).set_opacity(0)
        self.play(time1.animate.next_to(male1, UP).set_opacity(1))
        self.play(time2.animate.next_to(male2, UP).set_opacity(1))
        self.wait(2)

        cc7 = Text('เราเชื่อแบบนี้เป็นเวลามากกว่า 200 ปี', font='TH Sarabun New', font_size=35).move_to((0, -3, 0))
        self.replace(cc6, cc7)
        self.wait(4)

        cc8 = Text('จนมาถึงมือของนายอัลเบิร์ต ไอน์สไตน์ ที่จะพังทลายความเชื่อเหล่านี้', font='TH Sarabun New', font_size=35, t2c={'อัลเบิร์ต ไอน์สไตน์':RED}).move_to((0, -3, 0))
        rel_head = Text('ทฤษฎีสัมพัทธภาพพิเศษ', font='TH Sarabun New', font_size=75, color=RED).next_to((0, 4, 0), DOWN)
        rel_head_underline = Underline(rel_head, color=RED)
        einstein_png = ImageMobject('einstein.png').scale(2)
        self.replace(cc7, cc8)
        self.play(FadeOut(male1), FadeOut(male2), FadeOut(time1), FadeOut(time2), FadeIn(einstein_png), Write(rel_head), Write(rel_head_underline))
        self.wait(4)

        self.play(*[FadeOut(obj) for obj in self.mobjects])

        poem1 = Text(
            '๏ปัจจุบันทันสมัยวิจัยผล', font='TH Sarabun New', font_size=75, color='#ffeca1', slant=ITALIC,
            t2c={'ปัจจุบัน':GREEN}
        )
        poem2 = Text(
            'น่าฉงนความเร็วแสงสัมบูรณ์ไหน', font='TH Sarabun New', font_size=75, color='#ffeca1', slant=ITALIC,
            t2c={'ความเร็วแสงสัมบูรณ์':RED}
        ).next_to(poem1, DOWN)
        poem3 = Text(
            'ส่วนเวลากลายเป็นสัมพัทธ์ไป', font='TH Sarabun New', font_size=75, color='#ffeca1', slant=ITALIC,
            t2c={'เวลา':GOLD, 'สัมพัทธ์':GOLD}
        ).next_to(poem2, DOWN)
        poem4 = Text(
            'ปราชญ์บทใหม่แห่งทฤษฎีสัมพัทธภาพ๚ะ๛', font='TH Sarabun New', font_size=75, color='#ffeca1', slant=ITALIC,
            t2c={'ทฤษฎีสัมพัทธภาพ':PURPLE}
        ).next_to(poem3, DOWN)
        poemg = VGroup(poem1, poem2, poem3, poem4).move_to(ORIGIN)
        self.play(Write(poemg[0]), run_time=2)
        self.play(Write(poemg[1]), run_time=2)
        self.play(Write(poemg[2]), run_time=2)
        self.play(Write(poemg[3]), run_time=2)
        self.wait(3)
