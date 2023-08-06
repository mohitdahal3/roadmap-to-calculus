from manim import *
from math import sin ,cos

def Tick(x_pos , y_pos , color):
    l1 = Line(start=[x_pos+0.15,y_pos+0.39,0] , end=[x_pos+0.3,y_pos,0] , color=color)
    l2 = Line(start=[x_pos+0.3,y_pos,0] , end=[x_pos+1,y_pos+0.7,0] , color=color)
    return VGroup(l1,l2).scale(0.7).shift(UP*0.15)

class Scene1(Scene):
    def construct(self):
        
        slope = Text("2. Slope" , color=GREEN).scale(0.7).shift(LEFT * 1)
        functions = Text("1. Functions" , color=GREEN).scale(0.7).next_to(slope , UP , buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*2.5).align_to(slope , LEFT)
        infinity = Text("3. Infinitesimal &  Infinity").scale(0.7).next_to(slope , DOWN , buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*2.5).align_to(slope , LEFT)
        infinitytitle = Text("Infinitesimal &  Infinity" , color=BLUE).scale(0.8).to_edge(UP)
        t1 = Tick(0,0,YELLOW).next_to(functions , RIGHT , buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*2)
        t2 = Tick(0,0,YELLOW).next_to(slope , RIGHT , buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*2)

        desc = Text("Definitely not hard").scale(0.65).shift(UP * 1.5)

        self.wait()
        self.play(Write(functions))
        self.play(FadeIn(t1))
        self.play(Write(slope))
        self.play(FadeIn(t2))
        self.play(Write(infinity))

        self.play(FadeOut(*[slope , functions , t1 , t2]) , TransformMatchingShapes(infinity , infinitytitle))
        self.play(Write(desc))
        self.play(FadeOut(*[infinitytitle, desc]))



        self.wait()

class Scene2(Scene):
    def construct(self):
        title = Text("How to pronounce?").scale(0.7).to_edge(UP)
        p1 = Tex("in" , "fai" , "nite" , "si" , "mul" , arg_separator=" . " , color=BLUE)
        p2 = Tex("in" , "fin" , "teh" , "si" , "mul", arg_separator=" . " , color=BLUE)
        p3 = Tex("in" , "fi", "ni" , "teh" , "si" , "mul" , arg_separator=" . " , color=GREEN)
        p123 = VGroup(p1,p2,p3).arrange(DOWN , buff=0.75)  

        self.wait()
        self.play(Write(title))
        animations = [
            FadeIn(p1[0]),
            FadeIn(p1[1]),
            FadeIn(p1[2]),
            FadeIn(p1[3]),
            FadeIn(p1[4]),
        ]
        self.play(AnimationGroup(*animations , lag_ratio=0.5))
        animations = [
            FadeIn(p2[0]),
            FadeIn(p2[1]),
            FadeIn(p2[2]),
            FadeIn(p2[3]),
            FadeIn(p2[4]),
        ]
        self.play(AnimationGroup(*animations , lag_ratio=0.5))
        animations = [
            FadeIn(p3[0]),
            FadeIn(p3[1]),
            FadeIn(p3[2]),
            FadeIn(p3[3]),
            FadeIn(p3[4]),
            FadeIn(p3[5]),
        ]
        self.play(AnimationGroup(*animations , lag_ratio=0.5))
        self.play(FadeOut(*[p1 , p2]) , p3.animate.move_to(ORIGIN))
        self.play(FadeOut(p3 , title))

    

        self.wait()

class Scene3(Scene):
    def construct(self):
        # self.add(NumberPlane())
        infinity = Text("Infinity" , color=BLUE).to_edge(UP).scale(0.8)
        what = Text("What is").to_edge(UP).scale(0.8).shift(LEFT * 1.1)
        qmark = Text("?").to_edge(UP).scale(0.8).shift(RIGHT * 1.9)
        ans = Text("Infinity is the biggest number").scale(0.65)
        cross = Cross(ans , stroke_width=4)
        ax = Axes(
            x_range=[-10,10,1],
            y_range=[-10,10,1],
            x_length=21,
            y_length=21
        )
        symbol = ax.plot_parametric_curve(lambda t:[2*cos(t) * 0.4 , 0.7*sin(2*t) * 0.4] , t_range = [0.5 * PI,2.5*PI] , stroke_width = 2.5).shift(UP * 0.5)


        self.wait()
        self.play(Write(infinity))
        self.play(Create(symbol) , rate_func = linear)
        self.play(Write(what) , infinity.animate.shift(RIGHT * 0.85))
        self.play(Write(qmark))
        self.play(Write(ans) , FadeOut(symbol))
        self.play(Create(cross))
        self.play(FadeOut(ans , cross))


        self.wait()

class Scene4(Scene):
    def construct(self):
        infinity = Text("Infinity" , color=BLUE).to_edge(UP).scale(0.8).shift(RIGHT * 0.85)
        what = Text("What is").to_edge(UP).scale(0.8).shift(LEFT * 1.1)
        qmark = Text("?").to_edge(UP).scale(0.8).shift(RIGHT * 1.9)
        title = VGroup(infinity , what , qmark)
        think = Text("Think about the biggest number.").scale(0.65)
        notPossible = Text("(Not Possible!)" , color=YELLOW).scale(0.5).next_to(think , DOWN)
        eqn = MathTex(r"x" , "+" , "1" , ">" , "x" , color="GOLD").move_to(notPossible)

        self.add(title)
        self.wait()
        self.play(Write(think))
        self.play(FadeIn(notPossible))
        self.play(FadeOut(notPossible , scale = 1.35) , FadeIn(eqn[0]))
        animations = [
            FadeIn(eqn[1]),
            FadeIn(eqn[2]),
            FadeIn(eqn[3]),
            FadeIn(eqn[4])
        ]
        self.play(AnimationGroup(*animations , lag_ratio=0.7))
        self.play(FadeOut(*[think , eqn]))

        self.wait()

class Scene5(MovingCameraScene):
    def construct(self): 
        infinity = Text("Infinity" , color=BLUE).to_edge(UP).scale(0.8).shift(RIGHT * 0.85)
        what = Text("What is").to_edge(UP).scale(0.8).shift(LEFT * 1.1)
        qmark = Text("?").to_edge(UP).scale(0.8).shift(RIGHT * 1.9)
        title = VGroup(infinity , what , qmark)
        numberline = NumberLine(x_range=[-400 , 400 , 2] , length=400 , include_numbers=True , font_size = 20 , line_to_number_buff = 0.18)

        self.add(title)
        self.wait()
        self.play(FadeIn(numberline))
        self.play(self.camera.frame.animate.move_to([180 , 0 , 0]) , title.animate.shift(RIGHT*180) , rate_func = rush_into , run_time = 17)

        self.wait()

class Scene6(Scene):
    def construct(self):
        title = Text("How many numbers in the number line?" , color=BLUE).scale(0.7)
        implies = MathTex(r"\Rightarrow").scale(0.9).next_to(title , DOWN).align_to(title , LEFT).shift(LEFT * 0.64)
        ans = Text("Infinite").scale(0.5).next_to(implies , RIGHT)

        self.wait()
        self.play(Write(title))
        self.play(FadeIn(ans) , FadeIn(implies))

        self.play(Unwrite(title) , FadeOut(ans) , FadeOut(implies))
        


        self.wait()


class Scene7(Scene):
    def construct(self):
        # self.add(NumberPlane())
        title = Text("Answer this!" , color=BLUE).scale(0.8).to_edge(UP)
        qn = MathTex(r"\infty" , "+" ,  "1" ,  "=" ,  r"\;?" , color=GOLD).scale(0.8)
        apple = ImageMobject("apple.png").scale(0.05).shift(RIGHT * 2.45)

        box = Square(5 , stroke_width = 2)
        box2 = Rectangle(height=5 , width=5.25 , stroke_width = 2).shift(RIGHT * (0.25/2))
        apples = Group()
        for i in range(99):
            apples.add(ImageMobject("apple.png").scale(0.05))
        apples.add(MathTex(r"\cdots" , color=RED).scale(0.5))
        apples.arrange_in_grid(rows=10)

        self.wait()

        self.play(Write(title))
        animations = [
            FadeIn(qn[0]),
            FadeIn(qn[1]),
            FadeIn(qn[2]),
            FadeIn(qn[3]),
            FadeIn(qn[4])
        ]
        self.play(AnimationGroup(*animations , lag_ratio=0.4))
        self.play(qn.animate.move_to(title) , FadeOut(title))

        animations = []
        for i in range(100):
            animations.append(FadeIn(apples[i]))
        
        
        self.play(Create(box))
        
        self.play(AnimationGroup(*animations , lag_ratio=0.25) , run_time = 1)
        # self.add(apples)

        self.play(Transform(box , box2) , FadeIn(apple , shift=LEFT))
        self.play(FadeOut(apple , target_position = apples[99]) , Transform(box , Square(5 , stroke_width = 2)))


        self.wait()


class Scene8(Scene):
    def construct(self):
        title = Text("Answer this!" , color=BLUE).scale(0.8).to_edge(UP)
        qn = MathTex(r"\infty" , "+" ,  "1" ,  "=" ,  r"\;?" , color=GOLD).scale(0.8).move_to(title)
        qn2 = MathTex(r"\infty" , "+" ,  "1" ,  "=" ,  r"\infty" , color=GOLD).scale(0.8).move_to(title).scale(1.4)

        box = Square(5 , stroke_width = 2)
        apples = Group()
        for i in range(99):
            apples.add(ImageMobject("apple.png").scale(0.05))
        apples.add(MathTex(r"\cdots" , color=RED).scale(0.5))
        apples.arrange_in_grid(rows=10)


        self.add(*[qn , box , apples])
        self.wait()
        self.play(qn.animate.scale(1.4))
        self.play(Transform(qn , qn2))

        self.play(FadeOut(*[qn , box , apples]))


        self.wait()

class Scene9(Scene):
    def construct(self):
        qn = MathTex(r"\infty" , "-" ,  "1" ,  "=" ,  r"\;?" , color=GOLD).scale(0.9)
        box = Square(5 , stroke_width = 2)
        apples = Group()
        for i in range(99):
            apples.add(ImageMobject("apple.png").scale(0.05))
        apples.add(MathTex(r"\cdots" , color=RED).scale(0.5))
        apples.arrange_in_grid(rows=10)
        apple = ImageMobject("apple.png").scale(0.05).move_to(apples[89])
        index = Dot().move_to(apples[9])

        self.wait()
        self.play(Write(qn))
        self.play(qn.animate.to_edge(UP) , FadeIn(apples) , FadeIn(box))
        self.wait()
        self.play(apples[9].animate.shift(RIGHT * 1.5))
        self.wait()
        anims = [
            apples[19].animate.move_to(index),
            apples[29].animate.move_to(apples[19]),
            apples[39].animate.move_to(apples[29]),
            apples[49].animate.move_to(apples[39]),
            apples[59].animate.move_to(apples[49]),
            apples[69].animate.move_to(apples[59]),
            apples[79].animate.move_to(apples[69]),
            apples[89].animate.move_to(apples[79]),
        ]
        self.play(AnimationGroup(*anims , lag_ratio=(0.25)) , run_time = 1.3)
        self.play(FadeIn(apple , target_position = apples[99]))

        ans = MathTex(r"\infty" , "-" ,  "1" ,  "=" ,  r"\infty" , color=GOLD).scale(0.9).move_to(qn)
        self.play(Transform(qn , ans))
        self.play(FadeOut(box) , FadeOut(apples) , qn.animate.move_to([0,0,0]) , FadeOut(apple))
        

        self.wait()


class Scene10(Scene):
    def construct(self):
        qn = MathTex(r"\infty" , "-" ,  "1" ,  "=" ,  r"\infty" , color=GOLD).scale(0.9)
        ans = MathTex(r"\infty" , "-" ,  "1000000000" ,  "=" ,  r"\infty" , color=GOLD).scale(0.9)
        ans2 = MathTex(r"\frac{\infty}{2} = \infty" , color=GOLD).scale(0.9)
        natural = MathTex(r"\mathbb{N}atural\;numbers=" , color = BLUE)
        numbers = MathTex(r"\{1,\;2,\;3,\;4,\;5,\;\cdots\}" , color=BLUE)
        nn = VGroup(natural , numbers).arrange().scale(0.9)

        even = MathTex(r"Even\;numbers=" , color = BLUE)
        nums = MathTex(r"\{2,\;4,\;6,\;8,\;10,\;\cdots\}" , color=BLUE)
        en = VGroup(even , nums).arrange().shift(DOWN * 0.7).scale(0.9)

        self.add(qn)
        self.play(TransformMatchingShapes(qn , ans))
        self.play(TransformMatchingShapes(ans , ans2))

        self.play(FadeOut(ans2))
        self.play(Write(natural))
        self.play(Write(numbers))

        self.play(Write(even) , nn.animate.shift(UP * 0.7))
        self.play(Write(nums))

        self.play(Indicate(nn))
        self.play(Indicate(en))

        self.play(nn.animate.set_color("#0DA10E"))
        self.play(nn.animate.set_color(BLUE))

        inf1 = MathTex(r"\Rightarrow\;\infty").scale(0.85).next_to(nn)
        inf2 = MathTex(r"\Rightarrow\;\infty").scale(0.85).next_to(en)
        self.play(FadeIn(inf1))
        self.play(FadeIn(inf2))
        self.wait()

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )



        self.wait()


class Scene11(Scene):
    def construct(self):
        title = Text("What is Infinitesimal?" , color=BLUE, t2s={"Infinitesimal" : ITALIC}).scale(0.8).to_edge(UP)
        zero = MathTex("0" , r"\to").shift(LEFT * 0.2)
        point1 = MathTex(r"0.1?").next_to(zero , RIGHT)
        point01 = MathTex(r"0.01?").next_to(zero , RIGHT)
        ans = MathTex(r"0.0000000000000000000\cdots").next_to(zero , RIGHT)
        ans2 = MathTex(r"1").next_to(ans , RIGHT , buff=0.15)
        ans3 = MathTex(r"01").next_to(ans , RIGHT , buff=0.15)
        ans4 = MathTex(r"001").next_to(ans , RIGHT , buff=0.15)
        ans5 = MathTex(r"0001").next_to(ans , RIGHT , buff=0.15)
        ans6 = Tex("Infinitesimal").next_to(zero , RIGHT)

        self.wait()
        self.play(Write(title))
        self.wait()
        self.play(Write(zero))
        self.play(Write(point1))
        self.play(FadeOut(point1))

        self.play(Write(point01))
        self.play(FadeOut(point01))
        
        self.play(Write(ans) , run_time = 4.5)
        self.play(Write(ans2))

        self.play(TransformMatchingTex(ans2 , ans3))
        self.play(TransformMatchingTex(ans3 , ans4))
        self.play(TransformMatchingTex(ans4 , ans5))

        self.play(FadeOut(*[ans5 , ans]) , FadeIn(ans6))
        self.wait()
        self.play(FadeOut(*[zero , ans6]))
        
        self.wait()

class Scene12(Scene):
    def construct(self):
        title = Text("What is Infinitesimal?" , color=BLUE, t2s={"Infinitesimal" : ITALIC}).scale(0.8).to_edge(UP)
        ans = Tex("The "  , "number" ,  " right " , "after " ,  "Zero.")
        c = Cross(ans[1] , stroke_width=3)

        self.add(title)
        self.wait()
        self.play(Write(ans))
        self.play(Create(c))
        self.play(*[FadeOut(mob)for mob in self.mobjects])




        self.wait()