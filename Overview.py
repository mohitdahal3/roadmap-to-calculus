from manim import *
from math import sin , cos


def video_icon():
    t = Triangle(stroke_color=WHITE , fill_color=WHITE, fill_opacity = 1).rotate(-PI/2).scale(0.5).shift(RIGHT * 0.1 + DOWN * 0.25)
    box = RoundedRectangle(stroke_color=DARK_BLUE , fill_color=DARK_BLUE, fill_opacity = 1, corner_radius=0.4 , width=2, height=1.7)
    return VGroup(box,t)


def Tick(x_pos , y_pos , color):
    l1 = Line(start=[x_pos+0.15,y_pos+0.39,0] , end=[x_pos+0.3,y_pos,0] , color=color)
    l2 = Line(start=[x_pos+0.3,y_pos,0] , end=[x_pos+1,y_pos+0.7,0] , color=color)
    return VGroup(l1,l2).scale(0.7).shift(UP*0.15)

def Vec(x_pos , y_pos , l , theta):
    return Arrow(start = [x_pos , y_pos , 0] , end=[x_pos + l * cos(theta) , y_pos + l * sin(theta) ,0])


def Flag():
    triangle = Triangle(stroke_width = 0 , fill_color = YELLOW , fill_opacity = 1).rotate(PI/2)
    line = Line(UP * 1.6 , DOWN * 1.6, color=YELLOW , stroke_width = 2).next_to(triangle , RIGHT ,buff=0).align_to(triangle , UP).shift(DOWN * 0.008)
    base = Line(LEFT * 0.4 , RIGHT * 0.4, color=YELLOW , stroke_width = 2).next_to(line , DOWN , buff=0) 
    return VGroup(base , line , triangle)


class Scene1(ThreeDScene):
    def construct(self):
        helloText = Tex("Hello" , color=YELLOW)
        nameText = Tex(", " , "Mohit here").shift(RIGHT * 0.94)
        nameText[0].set_color(YELLOW)
        nameText[1].set_color(BLUE)
        uniqueHobby = Tex("Unique hobby" , color=BLUE)
        calculsText = Tex("Calculus" , color=YELLOW).scale(0.8).shift(UP * 3 + RIGHT * 0.7)
        flag = Flag().scale(0.2).next_to(calculsText , LEFT).align_to(calculsText , DOWN)
        titleText = Tex("Roadmap to Calculus" , color=BLUE).scale(1.3).rotate(65 * DEGREES , axis=X_AXIS)
        canvas = Rectangle(color=BLACK , height=10 , width=16 , stroke_width = 0).set_opacity(0.85)


        points = [ 
            [-0.85 , -1.9 , 0],
            [1.9 , 0.25 , 0],
            [-1.78 , 1.1 , 0],
            [0.3 , 2.91 , 0]
        ]
        path1 = CubicBezier(points[0] , points[1] , points[2] , points[3]).reverse_points().shift(LEFT + DOWN * 0.5)
        path2 = CubicBezier(points[0] , points[1] , points[2] , points[3]).reverse_points().shift(RIGHT + DOWN * 0.5)

        self.play(Write(helloText))
        self.wait()
        self.play(helloText.animate.shift(LEFT * 1) , Write(nameText))
        self.wait(2)
        self.play(FadeOut(helloText , nameText , run_time = 0.5) , Write(uniqueHobby))
        self.wait()
        self.play(Create(path1 , run_time = 1.3) , Create(path2 , run_time = 1.3) , FadeOut(uniqueHobby , run_time = 0.5))
        self.play(AnimationGroup( Write(calculsText , rate_func=linear) , GrowFromCenter(flag , rate_func = rush_into , run_time = 0.7) , lag_ratio=0.3) )
        self.play(Flash(flag[2].get_corner(DR), line_length=0.4, time_width=0.4 , run_time = 1 , rate_func = rush_from))
        self.wait()
        self.move_camera(phi=65*DEGREES)
        self.play(AnimationGroup(FadeIn(canvas) , Write(titleText) , lag_ratio=0.5) , rate_func=linear , run_time = 2)
        self.wait()
        

class Scene2(Scene):
    def construct(self):
        i1 = video_icon()
        i2 = video_icon()
        i3 = video_icon()
        i4 = video_icon()
        i5 = video_icon()
        i6 = video_icon()
        i7 = video_icon()
        i8 = video_icon()
        i9 = video_icon()

        iconGroup = VGroup(i1 , i2 , i3 , i4 , i5 , i6 , i7 , i8 , i9).arrange(buff=1.7).scale(0.4).to_edge(UP)
        iconGroupCopy = iconGroup.copy()
        text1 = Tex("Functions").scale(0.9).shift(DOWN * 1.3)
        text2 = Tex("Slope").scale(0.9).shift(DOWN * 1.3)
        text3 = Tex("Limits").scale(0.9).shift(DOWN * 1.3)
        text4 = Tex("Derivatives and Integrals").scale(0.9).shift(DOWN * 1.3)
        self.play(
            AnimationGroup(*[
                DrawBorderThenFill(iconGroup[i]) for i in range(iconGroup.__len__())
            ] , lag_ratio=0.5) , run_time = 1.2
        )

        self.play(i2.animate.move_to(ORIGIN).scale(2) , FadeIn(text1))

        self.wait(0.5)
        self.play(i2.animate.move_to(iconGroupCopy[1]).scale(0.5), i3.animate.move_to(ORIGIN).scale(2) , FadeTransform(text1 , text2))
        self.wait(0.5)
        self.play(i3.animate.move_to(iconGroupCopy[2]).scale(0.5), i5.animate.move_to(ORIGIN).scale(2) , FadeTransform(text2 , text3))
        self.wait(0.5)
        self.play(i5.animate.move_to(iconGroupCopy[4]).scale(0.5), VGroup(i8 , i9).animate.move_to(ORIGIN).scale(2) , FadeTransform(text3 , text4))
        self.wait(0.5)
        self.play(i8.animate.move_to(iconGroupCopy[7]).scale(0.5), i9.animate.move_to(iconGroupCopy[8]).scale(0.5) , FadeOut(text4))

        self.wait()

class Scene3(Scene):
    def construct(self):
        logo3b1b = ImageMobject('./3b1b.jpg').scale(0.3)
        # text = Text("3Blue1Brown" , t2c={'3Blue':BLUE , '1Brown':LIGHT_BROWN})
        text = Tex("3Blue", "1Brown" , color=LIGHT_BROWN).scale(1.3)
        text[0].set_color(BLUE)
        logo = Group(logo3b1b , text).arrange()
        self.play(FadeIn(logo3b1b) , Write(text))
        self.wait(2)
        self.play(FadeOut(logo))

        banner = ManimBanner().scale(0.4)
        self.play(banner.create())
        self.play(banner.expand())

        self.wait()

class Scene4(Scene):
    def construct(self):
        i1 = video_icon()
        i2 = video_icon()
        i3 = video_icon()
        i4 = video_icon()
        i5 = video_icon()
        i6 = video_icon()
        i7 = video_icon()
        i8 = video_icon()
        i9 = video_icon()

        iconGroup = VGroup(i1 , i2 , i3 , i4 , i5 , i6 , i7 , i8 , i9).arrange(buff=1.7).scale(0.4).to_edge(UP)
        self.add(iconGroup)

        self.play(
            AnimationGroup(*[
                iconGroup[i].animate(rate_func = there_and_back).shift(DOWN * 0.5) for i in range(1 , iconGroup.__len__())
            ] , lag_ratio=0.35)
        )
        self.wait()
        self.play(*[FadeOut(mob)for mob in self.mobjects])