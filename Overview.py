from manim import *
from math import sin , cos

def Tick(x_pos , y_pos , color):
    l1 = Line(start=[x_pos+0.15,y_pos+0.39,0] , end=[x_pos+0.3,y_pos,0] , color=color)
    l2 = Line(start=[x_pos+0.3,y_pos,0] , end=[x_pos+1,y_pos+0.7,0] , color=color)
    return VGroup(l1,l2).scale(0.7).shift(UP*0.15)

def Vec(x_pos , y_pos , l , theta):
    return Arrow(start = [x_pos , y_pos , 0] , end=[x_pos + l * cos(theta) , y_pos + l * sin(theta) ,0])

class Scene1(Scene):
    def construct(self):
        # self.add(NumberPlane())
        self.wait()
        welcome_guys = Tex("Welcome guys!",color=BLUE).scale(1.2)
        calculus = Tex("Calculus",color=GREEN)
        ar = Arrow(start=[-0.65,0,0] , end=[0.65,0,0])
        text = Tex("Math").shift(RIGHT*1.65)
        self.play(FadeIn(welcome_guys))
        self.wait()
        self.play(welcome_guys.animate.to_edge(UP),Write(calculus))
        self.play(calculus.animate.shift(LEFT*1.65) , FadeIn(ar) , FadeIn(text))
        self.play(FadeOut(text))
        text.become(Tex("Physics").shift(RIGHT*1.65))
        self.play(FadeIn(text))
        self.play(FadeOut(text))
        text.become(Tex("Economics").shift(RIGHT*1.65))
        self.play(FadeIn(text))
        self.play(FadeOut(text))
        text.become(Tex("Statistics").shift(RIGHT*1.65))
        self.play(FadeIn(text))
        self.play(FadeOut(text))
        text.become(Tex("Business").shift(RIGHT*1.65))
        self.play(FadeIn(text))
        self.play(FadeOut(text))
        text.become(Tex("Many Things!").shift(RIGHT*1.65).scale(0.75))
        self.play(FadeIn(text))

        
        self.play(FadeOut(calculus,text,ar))
        self.wait()


class Scene2(Scene):
    def construct(self):
        # self.add(NumberPlane())
        welcome_guys = Tex("Welcome guys!",color=BLUE).scale(1.2).to_edge(UP)
        self.add(welcome_guys)
        teacher = Tex("Teacher",color=GREEN).shift(UP*0.5)
        you = Tex("You",color=GREEN).shift(DOWN*0.5)
        t1 = Tick(1,0,YELLOW)
        t2 = Tick(1,-1,YELLOW)
        t3 = Tick(3 , -0.5 , WHITE)
        calculus = Tex("Calculus").shift(RIGHT * 2.1)
        ar = Arrow(start=[-1,0,0] , end=[1,0,0])
        self.play(Write(teacher))
        self.play(FadeIn(t1))
        self.play(Write(you))
        self.play(FadeIn(t2))
        
        self.play(teacher.animate.shift(LEFT * 3) , you.animate.shift(LEFT * 3) , t1.animate.shift(LEFT * 3) , t2.animate.shift(LEFT * 3) , FadeIn(ar))
        self.play(Write(calculus))
        self.play(FadeIn(t3))

        self.wait()


class Scene3(Scene):
    def construct(self):
        # self.add(NumberPlane())
        img = ImageMobject("3b1b.jpg").scale(0.35).shift(LEFT * 1.85)
        t = Tex('3Blue1Brown').next_to(img , RIGHT)
        
        self.play(FadeIn(img) , Write(t))

        self.wait()


class Scene4(Scene):
    def construct(self):
        # self.add(NumberPlane())
        l1 = Line(start=[-3,-2,0] , end=[-3,-1,0])
        l2 = Line(start=[-3,-1,0] , end=[-1,-1,0])
        l3 = Line(start=[-1,-1,0] , end=[-1,0,0])
        l4 = Line(start=[-1,0,0] , end=[1,0,0])
        l5 = Line(start=[1,0,0] , end=[1,1,0])
        l6 = Line(start=[1,1,0] , end=[3,1,0])
        f = Tex("Functions").shift(LEFT * 2 + DOWN * 0.5).scale(0.9)
        l = Tex("Limits").shift(UP * 0.5)
        c = Tex("Calculus").shift(RIGHT * 2 + UP * 1.5)

        self.play(FadeIn(l1,l2)) 
        self.play(Write(f))
        self.play(FadeIn(l3,l4)) 
        self.play(Write(l))
        self.play(FadeIn(l5,l6)) 
        self.play(Write(c))

        a = Vec(-3,0,4.5,0.46)
        self.play(Create(a))
        self.wait()