from manim import*
import random


def random_2d_position(xrange , yrange):
    xdiff = (xrange[1] - xrange[0])
    xcoord = (random.random() * xdiff) + xrange[0]
    
    ydiff = (yrange[1] - yrange[0])
    ycoord = (random.random() * ydiff) + yrange[0]
    return [round(xcoord , 3) , round(ycoord , 3) , 0]




class Scene1(Scene):
    def construct(self):
        # self.add(NumberPlane())
        functionbox = Rectangle(width=5.333, height=3 , color=YELLOW , stroke_width=2).scale(0.8)
        slopebox = Rectangle(width=5.333, height=3 , color=YELLOW , stroke_width=2).scale(0.8)
        limitbox = Rectangle(width=5.333, height=3 , color=YELLOW , stroke_width=2).scale(0.8)


        boxes = VGroup(functionbox , slopebox , limitbox).arrange(buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER * 1.8)

        functiontext = Tex("Function" , color=BLUE).next_to(functionbox , DOWN)
        slopetext = Tex("Slope" , color=BLUE).next_to(slopebox , DOWN)
        limittext = Tex("Limit" , color=BLUE).next_to(limitbox , DOWN)


        self.wait()
        self.play(FadeIn(boxes[0]))
        self.play(Write(functiontext))
        self.play(FadeIn(boxes[1]))
        self.play(Write(slopetext))
        self.play(FadeIn(boxes[2]))
        self.play(Write(limittext))        


        self.wait()

class Scene2(Scene):
    def construct(self):
        def areacurve(x):
            a = 1.1
            b = -0.4
            c = -1.5
            d = 1.6
            return (a*(x**3)) + (b*(x**2)) + (c*x) + d
        

        title = Text("What is Calculus?" , color=BLUE).scale(0.8).to_edge(UP)
        ans1 = Text("Well,").scale(0.6)
        ans2 = Text("It's related to change." , t2c={"change":YELLOW}).scale(0.6)
        VGroup(ans1 , ans2).arrange()
        # NumberLine()
        axes1 = Axes(x_range=[-3,3,1] , y_range=[-3,3,1] , x_length=5 , y_length=5 , axis_config={'include_tip':False}).shift(LEFT * 3.5)
        axes2 = Axes(x_range=[-3,3,1] , y_range=[-3,3,1] , x_length=5 , y_length=5 , axis_config={'include_tip':False}).shift(RIGHT * 3.5)

        slopeline = axes1.plot(lambda x : x , x_range=[-2.5,2.5] , stroke_width = 2 , color=BLUE)
        slopetext = MathTex(r"Slope = 1" , color = BLUE).scale(0.6).move_to(axes1.coords_to_point(-1.5,1))


        arealine = axes2.plot(areacurve , x_range=[-1.7,1.6] , stroke_width = 2 , color=RED)
        area = axes2.get_area(arealine , x_range=[-1.383 , 0.8] , stroke_width = 0 , color = [GREEN_A , BLUE_B] , opacity = 0.55)

        self.wait()
        self.play(Write(title))
        self.play(Write(ans1))
        self.wait(0.1)
        self.play(Write(ans2))
        self.play(FadeOut(*[ans1 , ans2]))

        self.play(FadeIn(axes1))
        self.play(Create(slopeline) , Write(slopetext))


        self.play(FadeIn(axes2))
        self.play(Create(arealine))
        self.play(FadeIn(area))
        self.wait()

        self.play(FadeOut(*[axes1 , axes2 , slopeline , slopetext , arealine , area]))

class Scene3(Scene):
    def construct(self):
        # self.add(NumberPlane())
        title = Text("What is Calculus?" , color=BLUE).scale(0.8).to_edge(UP)

        t1 = Tex("Derivative" , color = random_bright_color()).move_to(random_2d_position(xrange=[-4,4] , yrange=[-3,2.5]))  
        t2 = Tex("Integration" , color = random_bright_color()).move_to(random_2d_position(xrange=[-4,4] , yrange=[-3,2.5]))  
        t3 = MathTex(r"\Delta x" , color = random_bright_color()).move_to(random_2d_position(xrange=[-4,4] , yrange=[-3,2.5]))
        t4 = MathTex(r"\Delta y" , color = random_bright_color()).move_to(random_2d_position(xrange=[-4,4] , yrange=[-3,2.5]))
        t5 = MathTex(r"\frac{d}{dx} x^{n} = nx^{n-1}" , color = random_bright_color()).move_to(random_2d_position(xrange=[-4,4] , yrange=[-3,2.5]))
        t6 = MathTex(r"\frac{dy}{dx} = \frac{dy}{du}\frac{du}{dx}" , color = random_bright_color()).move_to(random_2d_position(xrange=[-4,4] , yrange=[-3,2.5]))  
        t7 = Tex("Slope of Tangent" , color = random_bright_color()).move_to(random_2d_position(xrange=[-4,4] , yrange=[-3,2.5]))  
        t8 = MathTex(r"\int udv = uv - \int vdu" , color = random_bright_color()).move_to(random_2d_position(xrange=[-4,4] , yrange=[-3,2.5]))  
        t9 = MathTex(r"\int du = u" , color = random_bright_color()).move_to(random_2d_position(xrange=[-4,4] , yrange=[-3,2.5]))  

        self.add(title)


        self.wait()

        self.add(t1)
        self.wait(0.2)
        self.play(AnimationGroup(*[FadeOut(t1 , run_time = 2) , FadeIn(t2 , run_time = 0.1)] , lag_ratio=0.6))
        self.play(AnimationGroup(*[FadeOut(t2 , run_time = 2)]))
        self.play(FadeIn(t3 , run_time = 0.1))
        self.play(AnimationGroup(*[FadeOut(t3 , run_time = 2) , FadeIn(t4 , run_time = 0.1)] , lag_ratio=0.6))
        self.play(AnimationGroup(*[FadeOut(t4 , run_time = 1.5) , FadeIn(t5 , run_time = 0.1)] , lag_ratio=0.5))
        self.play(AnimationGroup(*[FadeOut(t5 , run_time = 1.5) , FadeIn(t6 , run_time = 0.1)] , lag_ratio=0.5))
        self.play(AnimationGroup(*[FadeOut(t6 , run_time = 1.5) , FadeIn(t7 , run_time = 0.1)] , lag_ratio=0.6))
        self.play(AnimationGroup(*[FadeOut(t7 , run_time = 2) , FadeIn(t8 , run_time = 0.1)] , lag_ratio=0.9))
        self.play(AnimationGroup(*[FadeOut(t8 , run_time = 1.5)]))
        self.play(FadeIn(t9 , run_time = 0.1))
        self.play(FadeOut(t9 , run_time = 1.5))


        self.wait()
        


class Scene4(Scene):
    def construct(self):
        title = Text("What is Calculus?" , color=BLUE).scale(0.8).to_edge(UP)
        title2 = Text("Timeline" , color=BLUE).scale(0.8).to_edge(UP)
        timeline = NumberLine(x_range=[1650 , 2030 , 1] , unit_size=1.75 , include_numbers=True,
            decimal_number_config={"num_decimal_places":0 , "group_with_commas": False} , 
            numbers_with_elongated_ticks=[2023 , 1660]).shift(LEFT * 320.25)
        label = Tex("(Present Year)" , color=YELLOW).shift(UP * 0.5).scale(0.65)
        arrow = Arrow(start = timeline.n2p(1660) + UP * 2 , end = timeline.n2p(1660))
        label2 = Tex("(Discovery of Calculus!)" , color=YELLOW).scale(0.65).next_to(arrow , UP)


        self.add(title)
        self.wait()
        self.play(Transform(title , title2) , FadeIn(timeline) , FadeIn(label))
        # self.play(FadeIn(timeline) , FadeIn(label))
        self.play(timeline.animate.shift(RIGHT * 635.25) , label.animate.shift(RIGHT * 635.25) , arrow.animate.shift(RIGHT * 635.25) , label2.animate.shift(RIGHT * 635.25))

        self.wait()

class  Scene5(Scene):
    def construct(self):
        title = Text("Timeline" , color=BLUE).scale(0.8).to_edge(UP)
        timeline = NumberLine(x_range=[1650 , 2030 , 1] , unit_size=1.75 , include_numbers=True,
            decimal_number_config={"num_decimal_places":0 , "group_with_commas": False} , 
            numbers_with_elongated_ticks=[2023 , 1660]).shift(LEFT * 320.25 + RIGHT * 635.25)
        arrow = Arrow(start = timeline.n2p(1660) + UP * 2 , end = timeline.n2p(1660))
        label = Tex("(Discovery of Calculus!)" , color=YELLOW).scale(0.65).next_to(arrow , UP)
        newton = ImageMobject('sir-isaac-newton.png').scale(0.42).shift(DOWN * 1.75 + LEFT * 2.5)
        leibniz = ImageMobject('gottfried.jpg').scale(0.0741).shift(DOWN * 1.75 + RIGHT * 2.5)
        nname = Text("Sir Isaac Newton").scale(0.5).next_to(newton , DOWN , buff=0.1)
        lname = Text("Gottfried Wilhelm Leibniz").scale(0.5).next_to(leibniz , DOWN , buff=0.1)

        self.add(title , timeline , arrow , label)
        self.play(AnimationGroup(*[FadeIn(newton) , Write(nname)] , lag_ratio=0.5))
        self.play(AnimationGroup(*[FadeIn(leibniz) , Write(lname)] , lag_ratio=0.5))
        self.wait()
        self.play(*[FadeOut(mob)for mob in self.mobjects])


class Scene6(Scene):
    def construct(self):
        imp = Text("The Essence of Calculus!" , color=BLUE).scale(0.8)
        ease_out_cubic
        self.play(Write(imp))

        self.wait()
