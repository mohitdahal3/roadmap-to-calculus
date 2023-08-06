from manim import *
from math import exp,log,sin

def video_icon():
    t = Triangle(stroke_color=WHITE , fill_color=WHITE, fill_opacity = 1).rotate(-PI/2).scale(0.5).shift(RIGHT * 0.1 + DOWN * 0.25)
    box = RoundedRectangle(stroke_color=DARK_BLUE , fill_color=DARK_BLUE, fill_opacity = 1, corner_radius=0.4 , width=2, height=1.7)
    return VGroup(box,t)

def machine():
    box = Rectangle(fill_color=BLUE, fill_opacity=1 , stroke_color=BLUE, height=1, width=2)
    inp = Rectangle(fill_color=BLUE, stroke_color=BLUE ,fill_opacity=1 , height=0.5 , width=0.35).shift(LEFT*0.5 + UP * 0.75)
    outp = Rectangle(fill_color=BLUE, stroke_color=BLUE ,fill_opacity=1 , height=0.5 , width=0.35).shift(RIGHT*0.5 + DOWN * 0.75)
    return VGroup(inp , outp , box)


class Scene1(Scene):
    def construct(self):
        welcome = Tex("Welcome back!", color=BLUE).scale(1.2)
        roadmap_to_calculus = Tex("Roadmap to Calculus: ",color=WHITE).scale(0.85).shift(LEFT * 3.56)
        icon1 = video_icon()
        icon2 = video_icon()
        icon3 = video_icon()
        icon4 = video_icon()
        icon5 = video_icon()
        icons = Group(icon1 , icon2 , icon3 , icon4 , icon5 , Dot() , Dot() , Dot()).arrange(buff = 1).scale(0.4).shift(RIGHT*2.4)


        self.wait()
        self.play(Write(welcome))
        self.wait()
        self.play(welcome.animate.to_edge(UP))
        self.play(FadeIn(roadmap_to_calculus), FadeIn(icons))
        self.wait(0.5)
        self.play(Wiggle(icon2 , scale_value=1.3, rotation_angle=0.03*TAU , run_time=2.5))
        self.wait()
        self.play(FadeOut(icons , welcome , roadmap_to_calculus))

class Scene2(Scene):
    def construct(self):
        # self.add(NumberPlane())
        what = Tex("What is a Function?" , color=BLUE).scale(1.3).to_edge(UP)
        machine_icon = machine()
        text = Text("Machine",color=PURE_BLUE, font="calibri").scale(0.7)
        input_arrow = Arrow(start=[-0.5 , 1.7 , 0] , end=[-0.5 , 1.2 , 0] , buff=0 , color=GOLD)
        output_arrow = Arrow(start=[0.5 , -1.2 , 0] , end=[0.5 , -1.7 , 0] , buff=0 , color=GOLD)
        input_set = Text("{a , b , c , d , ...}" , font="sans-serif").scale(0.4).shift([-0.5,1.4,0])
        output_set = Text("{A , B , C , D , ...}" , font="sans-serif").scale(0.35).shift([0.5,-1.4,0])
        domain_text = Text("Domain" , font="sans-serif").scale(0.5).shift([2,1.4,0])
        range_text = Text("Range" , font="sans-serif").scale(0.5).shift([3,-1.4,0])
        domain_arrow = Arrow(start = [0.7,1.4,0] , end = [1.3 , 1.4 , 0] , color = BLUE , buff=0)
        range_arrow = Arrow(start = [1.7,-1.4,0] , end = [2.3,-1.4,0] , color = BLUE , buff=0)
        # x = Text("𝑥" , font="sans-serif" , slant=ITALIC).scale(0.5).move_to(input_set)
        x = MathTex(r"x").scale(0.7).move_to(input_set)
        y = MathTex(r"y").scale(0.7)
        or_text = Text("or").scale(0.5)
        fx = MathTex(r"f(x)").scale(0.7)
        yorfx = VGroup(y,or_text,fx).arrange(buff=0.2).move_to(output_set)
        

        self.wait()
        self.play(Write(what) , run_time = 1.5)
        self.play(FadeIn(machine_icon))
        self.play(Write(text))
        self.play(DrawBorderThenFill(input_arrow) , run_time = 1)
        self.play(FadeOut(input_arrow , shift = DOWN))
        self.play(FadeIn(output_arrow , shift = DOWN))
        self.play(Uncreate(output_arrow))
        self.play(FadeIn(input_set))

        animations = [
            FadeIn(domain_arrow , shift = RIGHT), 
            Write(domain_text)
        ]

        self.play(AnimationGroup(*animations , lag_ratio=0.3))

        self.play(FadeIn(output_set))

        animations = [
            FadeIn(range_arrow , shift = RIGHT), 
            Write(range_text)
        ]

        self.play(AnimationGroup(*animations , lag_ratio=0.3))

        self.wait()

        self.play(FadeOut(input_set,scale=3) , FadeIn(x , scale=0.4) , FadeOut(domain_arrow) , FadeOut(domain_text))
        self.play(FadeOut(output_set,scale=3) , FadeIn(yorfx , scale=0.4) , FadeOut(range_arrow) , FadeOut(range_text))

        self.play(FadeOut(machine_icon) , FadeOut(x) , FadeOut(yorfx) , FadeOut(text))

        x.move_to([0,0,0]).scale(1.4)
        y.move_to([0,0,0]).scale(1.4).set_color(BLUE)
        func = Tex("Function").shift(UP * 0.2).scale(0.7).set_color_by_gradient(BLUE_A , BLUE)

        arr = Arrow(buff = 0 , start=LEFT * 1.1 , end = RIGHT*1.1)

        relation = VGroup(x , arr , y).arrange(buff=0.3).shift(RIGHT * 0.15)
        self.play(Write(relation))
        self.play(Write(func))
        self.play(what.animate.shift(UP * 6) , relation.animate.shift(UP * 6) , func.animate.shift(UP * 6))



class Scene3(Scene):
    def construct(self):
        # self.add(NumberPlane())
        example_text = Text("Time for an Example!" , color=BLUE).scale(0.7).to_edge(UP)
        equation = MathTex(r"y" ,  r"=", r"2", r"x")
        equation[0].set_color(BLUE)
        equation[2].set_color(RED)
        input_set = VGroup()
        for i in range(-3,4):
            input_set.add(MathTex(f"{i}"))
        input_set.arrange(direction=DOWN , buff=0.45).scale(0.7).shift(LEFT * 1.25 + DOWN * 0.24)

        output_set = VGroup()
        for i in range(-6,7,2):
            output_set.add(MathTex(f"{i}" , color=BLUE))
        output_set.arrange(direction=DOWN , buff=0.45).scale(0.7).shift(RIGHT * 1.25 + DOWN * 0.24)
        domain_oval = Ellipse(width=1.2 , height=4 , color = WHITE).move_to(input_set)
        range_oval = Ellipse(width=1.2 , height=4 , color = BLUE).move_to(output_set)
        domain_text = Text("Domain" , color=WHITE).scale(0.55).next_to(domain_oval , DOWN)
        range_text = Text("Range" , color=BLUE).scale(0.55).next_to(range_oval , DOWN)
        curveline = Arc(radius = 2 , start_angle=PI-(PI/3.15) , angle=(-23*PI)/63)
        tri = Triangle(stroke_color=WHITE , fill_color=WHITE, fill_opacity = 1).rotate(-PI/2).scale(0.15).shift(UP * 1.75)

        self.wait()
        self.play(Write(example_text) , run_time = 1.5)
        self.play(FadeIn(equation))
        self.play(Indicate(equation[3],scale_factor=1.3))
        self.play(Indicate(equation[2],scale_factor=1.3))
        self.play(Indicate(equation[0],scale_factor=1.3))
        self.play(equation.animate.next_to(example_text , DOWN , buff=0.4))


        self.play(Write(input_set) , run_time = 2)
        animations = []
        for i in range(7):
            animations.append(TransformFromCopy(input_set[i] , output_set[i]))

        self.play(AnimationGroup(*animations , lag_ratio=0.4))    
        self.play(FadeIn(domain_oval))
        self.play(Write(domain_text))

        self.play(FadeIn(range_oval))
        self.play(Write(range_text))

        self.play(Create(curveline) , FadeIn(tri))
        self.wait()


class Scene4(Scene):
    def construct(self):
        # self.add(NumberPlane())
        title = Text("Graphing a Function!" , color=BLUE).scale(0.8).to_edge(UP)
        ans = Text("Graph of a function is the visual representation of the function.").scale(0.5).shift(UP)
        xaxis = Line(start = [-5,0,0] , end=[5,0,0])
        yaxis = Line(start = [0,3.5,0] , end=[0,-3.5,0])
        xaxis_text = Text("x-axis").scale(0.4).move_to([4.5,0.2,0])
        yaxis_text = Text("y-axis").scale(0.4).move_to([-0.5,3.25,0])
        x = NumberLine(
            x_range=[-20 , 20 , 2],
            length=10,
            color=WHITE,
            include_numbers=True,
            label_direction=DOWN,
            include_tip=True,
            font_size=17,
            tip_height=0.1,
            tip_width=0.1,
            tick_size=0.08,
            line_to_number_buff=0.15,
            numbers_to_exclude=[0],
        )


        y = NumberLine(
            x_range=[-14 , 14 , 2],
            length=7,
            color=WHITE,
            include_numbers=True,
            label_direction=LEFT,
            include_tip=True,
            font_size=17,
            tip_height=0.1,
            tip_width=0.1,
            tick_size=0.08,
            line_to_number_buff=0.15,
            rotation=PI/2,
            numbers_to_exclude=[0],
        )

        ax = Axes(
            x_range=[-20,20,2],
            y_range=[-14,14,2],
            x_length=10,
            y_length=7
        )

        curve = ax.plot(lambda x:2 * x , x_range=(-5,5) , color = BLUE)
        equation = MathTex(r"y = 2x" , color = RED).scale(0.5).move_to([1.25 , 2.75 , 0]).set_color_by_gradient(BLUE , BLUE_A , WHITE)

        input_set = VGroup()
        for i in range(-3,4):
            input_set.add(MathTex(f"{i}"))
        input_set.arrange(direction=DOWN , buff=0.45).scale(0.7).shift(LEFT * 1.25 + DOWN * 0.24)

        output_set = VGroup()
        for i in range(-6,7,2):
            output_set.add(MathTex(f"{i}" , color=BLUE))
        output_set.arrange(direction=DOWN , buff=0.45).scale(0.7).shift(RIGHT * 1.25 + DOWN * 0.24)
        domain_oval = Ellipse(width=1.2 , height=4 , color = WHITE).move_to(input_set)
        range_oval = Ellipse(width=1.2 , height=4 , color = BLUE).move_to(output_set)
        curveline = Arc(radius = 2 , start_angle=PI-(PI/3.15) , angle=(-23*PI)/63)
        tri = Triangle(stroke_color=WHITE , fill_color=WHITE, fill_opacity = 1).rotate(-PI/2).scale(0.15).shift(UP * 1.75)



        map_diagram = VGroup(input_set , output_set , domain_oval , range_oval , curveline , tri).scale(0.65).shift(DOWN * 2 + RIGHT * 2.5)
        p1 = Dot(color=BLUE , radius=0.04).move_to([-0.75,-1.5,0])
        p2 = Dot(color=BLUE , radius=0.04).move_to([-0.5 , -1 , 0])
        p4 = Dot(color=BLUE , radius=0.04).move_to([0,0,0])
        p3 = Dot(color=BLUE , radius=0.04).move_to([-0.25 , -0.5 , 0])
        p5 = Dot(color=BLUE , radius=0.04).move_to([0.25,0.5,0])
        p6 = Dot(color=BLUE , radius=0.04).move_to([0.5 , 1 , 0])
        p7 = Dot(color=BLUE , radius=0.04).move_to([0.75 , 1.5 , 0])





        self.play(Write(title))
        self.wait(0.5)
        self.play(AddTextLetterByLetter(ans) , run_time = 3.5)
        self.wait(1.5)
        self.play(Unwrite(ans) , Unwrite(title) , run_time = 0.85)
        self.play(Create(xaxis))
        self.play(Create(yaxis))
        self.play(Write(xaxis_text))
        self.play(Write(yaxis_text))

        self.play(Create(x) , Create(y))
        self.play(FadeIn(map_diagram))

        self.play(Indicate(input_set[0],scale_factor=1.5) , run_time = 0.8)
        self.play(Indicate(output_set[0],scale_factor=1.5) , run_time = 0.8)
        self.play(FadeIn(p1))


        self.play(Indicate(input_set[1],scale_factor=1.5) , run_time = 0.8)
        self.play(Indicate(output_set[1],scale_factor=1.5) , run_time = 0.8)
        self.play(FadeIn(p2))

        self.play(FadeIn(p3) , run_time = 0.4)
        self.play(FadeIn(p4) , run_time = 0.4)
        self.play(FadeIn(p5) , run_time = 0.4)
        self.play(FadeIn(p6) , run_time = 0.4)
        self.play(FadeIn(p7) , run_time = 0.4)

        self.play(Create(curve))
        self.play(Write(equation))


        self.wait(2.5)

        self.play(
            FadeOut(title),
            FadeOut(xaxis),
            FadeOut(yaxis),
            FadeOut(xaxis_text),
            FadeOut(yaxis_text),
            FadeOut(x),
            FadeOut(y),
            FadeOut(curve),
            FadeOut(equation),
            FadeOut(map_diagram),
            FadeOut(p1),
            FadeOut(p2),
            FadeOut(p3),
            FadeOut(p4),
            FadeOut(p5),
            FadeOut(p6),
            FadeOut(p7),
        )
        self.wait()


        
class Scene5(Scene):
    def construct(self):
        pause_and_ponder = Text("Time to Pause and Ponder!" , color=BLUE).scale(0.85)
        equation = MathTex("y = 2x").scale(0.9)
        equation2 = MathTex("y = 3x").scale(0.9).shift(LEFT * 1.7)
        equation3 = MathTex("y = 5x").scale(0.9).shift(LEFT * 1.7)
        equation4 = MathTex("y = 0.5x").scale(0.9).shift(LEFT * 1.7)
        equation5 = MathTex(r"y = (some\;constant)x").scale(0.9).shift(LEFT * 3.2)
        text = Text("Linear Function" , color=BLUE).shift(RIGHT * 2.6).scale(0.7)
        arr = Arrow(start = [LEFT] , end = [RIGHT])



        self.play(Write(pause_and_ponder))
        self.wait(0.5)
        self.play(ApplyWave(pause_and_ponder))
        self.wait(0.5)
        self.play(ApplyWave(pause_and_ponder))
        self.wait(0.5)
        self.play(ApplyWave(pause_and_ponder))
        self.wait()
        self.play(FadeOut(pause_and_ponder))

        self.play(Write(equation))
        self.play(equation.animate.shift(LEFT * 1.7) , FadeIn(arr) , Write(text))
        self.play(TransformMatchingTex(equation , equation2))
        self.play(TransformMatchingTex(equation2 , equation3))
        self.play(TransformMatchingTex(equation3 , equation4))
        self.play(TransformMatchingTex(equation4 , equation5))
        self.play(FadeOut(equation5) , FadeOut(text) , FadeOut(arr))

        self.wait()


class Scene6(Scene):
    def construct(self):
        equation = MathTex("y = x^2")
        ax = Axes(
            x_range=[-5,5,1],
            y_range=[-1,5,1],
            x_length=10,
            y_length=6,
            axis_config={"include_numbers": True , "font_size":20},
        )
        ax2 = Axes(
            x_range=[-7,7,1],
            y_range=[-4,4,1],
            x_length=14,
            y_length=8,
            axis_config={"include_numbers": True , "font_size":20},
        )
        quadratic = Text("Quadratic Function").move_to([3.5,0,0]).scale(0.5)
        text = Text("Exponential Function:").move_to([3.5,-2,0]).scale(0.5)

        curve = ax.plot(lambda x:x*x , x_range=(-2.25,2.25) , color = BLUE)


        self.play(Write(equation))
        self.play(equation.animate.shift(UP*3.5))
        self.play(Create(ax))
        self.play(Create(curve))
        self.wait(3)
        self.play(Write(quadratic))
        self.wait()
        self.play(FadeOut(equation) , FadeOut(quadratic) , FadeOut(curve))
        self.play(Transform(ax , ax2))



        equation = MathTex("y = e^x").next_to(text , DOWN)
        curve = ax2.plot(lambda x:exp(x) , x_range=(-7,7) , color=BLUE)
        self.play(Create(curve , run_time = 2) , Write(text) , Write(equation))

        equation2 = MathTex("y = ln(x)").move_to(equation)
        text2 = Text("Logarithmic Function:").move_to(text).scale(0.5)
        curve2 = ax2.plot(lambda x:log(x) , x_range=(0.001,7) , color=BLUE , use_smoothing=False)

        animations = [
            TransformMatchingTex(equation , equation2),
            ReplacementTransform(text , text2),
            ReplacementTransform(curve , curve2)
        ]
        self.wait(2)
        self.play(AnimationGroup(*animations))




        equation3 = MathTex("y = sin(x)").move_to(equation)
        text3 = Text("Trigonometric Function:").move_to(text).scale(0.5)
        curve3 = ax2.plot(lambda x:sin(x) , x_range=(-7,7) , color=BLUE , use_smoothing=True)

        animations = [
            TransformMatchingTex(equation2 , equation3),
            ReplacementTransform(text2 , text3),
            ReplacementTransform(curve2 , curve3)
        ]
        self.wait(2)
        self.play(AnimationGroup(*animations))





        equation4 = MathTex(r"(2\text{cos}\;t \; ,2\text{sin}\;t) \;\; ,\; \{0 \le t \le 2\pi\}").move_to(equation).scale(0.8)
        text4 = Text("Parametric Function:").move_to(text).scale(0.5)
        curve4 = Circle(radius=2 , stroke_color = BLUE , fill_opacity = 0)

        animations = [
            TransformMatchingTex(equation3 , equation4),
            ReplacementTransform(text3 , text4),
            ReplacementTransform(curve3 , curve4)
        ]
        self.wait(2)
        self.play(AnimationGroup(*animations))


        self.wait(2)

        self.play(FadeOut(curve4) , FadeOut(text4) , FadeOut(equation4) , FadeOut(ax) , FadeOut(ax2))

class Scene7(Scene):
    def construct(self):

        img = ImageMobject("Desmos logo.png").scale(0.5)
        text = Text("desmos.com" , color=WHITE).scale(0.6).shift(RIGHT * 1.5)
        self.wait()
        self.play(FadeIn(img))
        self.play(img.animate.shift(LEFT) , Write(text))
        self.wait()
        self.play(FadeOut(img) , FadeOut(text))


class Outro(Scene):
    def construct(self):
        subs = Text("Subscribe!").scale(0.75)
        c = Circle(color=WHITE)
        outro = VGroup(c , subs).arrange(buff = 0.6)
        self.wait()
        self.play(FadeIn(outro))

        for i in range(4):
            self.play(Flash(
                c,
                line_length=0.3,
                flash_radius=1.15,
                num_lines=15,
                
            ))
            self.wait(1.5)
        self.wait()




class Intro(Scene):
    def construct(self):
        logo = ImageMobject("./learnwithus.png").scale(0.5)
        text = Text("Learn With Us" , font="Comic Sans MS" , font_size=17 , fill_opacity=1 , fill_color=BLACK , stroke_width=1.3 , stroke_color = "#29ABCA").shift(DOWN * 1.75)
        self.wait()
        self.play(FadeIn(logo))
        self.play(Write(text))
        self.wait()