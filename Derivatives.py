from manim import *
from math import floor,exp,sin,cos,sqrt


def LineThroughPoints(point1 , point2 , x_range=None, line_length=None, **mykwargs):
    slope = (point2[1] - point1[1])/(point2[0] - point1[0])

    def y(x):
        return (slope * (x - point1[0])) + point1[1]
    
    if(line_length==None):
        return Line(start= [x_range[0] , y(x_range[0]) , 0] , end = [x_range[1] , y(x_range[1]) , 0] , **mykwargs)
    else:
        my_x_range_length = sqrt( (pow(line_length/2 , 2)) / (1 + (slope * slope)) )
        my_x_range = [point1[0] - my_x_range_length , point2[0] + my_x_range_length]
        return Line(start= [my_x_range[0] , y(my_x_range[0]) , 0] , end = [my_x_range[1] , y(my_x_range[1]) , 0] , **mykwargs)



def Speedometer():
    radius = 1.5
    arc = Arc(radius=radius , start_angle=215*DEGREES , angle=-250*DEGREES , stroke_width = 3)
    center = Dot(radius=DEFAULT_SMALL_DOT_RADIUS)
    n1 = MathTex("0").scale(0.5)
    n2 = MathTex("10").scale(0.5)
    n3 = MathTex("20").scale(0.5)
    n4 = MathTex("30").scale(0.5)
    n5 = MathTex("40").scale(0.5)
    n6 = MathTex("50").scale(0.5)
    n7 = MathTex("60").scale(0.5)
    n8 = MathTex("70").scale(0.5)
    n9 = MathTex("80").scale(0.5)
    numbers = VGroup(n1,n2,n3,n4,n5,n6,n7,n8,n9)

    ticks = VGroup()
    for i in range(9):
        ticks.add(Line(start=UP * 0.05 , end=DOWN * 0.07 , stroke_width = 2).shift(UP * radius))

    currentAngle = 210
    for i in range(9):
        numbers[i].shift([(radius+0.2) * cos(currentAngle * DEGREES) , (radius+0.2) * sin(currentAngle*DEGREES) , 0])
        ticks[i].rotate((currentAngle*DEGREES) - (PI/2) , about_point=ORIGIN)
        currentAngle = currentAngle-30

    speedometer = VGroup(arc , ticks , numbers , center)
    return speedometer



def myconstrain(value , minimum , maximum):
    if(value > maximum):
        return maximum
    elif(value < minimum):
        return minimum
    else:
        return value


def positionFunction(t , inflection = 12.5):
    error = sigmoid(-inflection / 2)
    return 50 * myconstrain( (sigmoid(inflection * ((t/5) - 0.5)) - error) / (1 - 2 * error) , 0 , 1)

def velocityFunction(t):
    return (31.36 * exp(-(t - 2.5) * (t - 2.5) * 1.081315))

def mySmooth(t , inflection = 12.5):
    error = sigmoid(-inflection / 2)
    return myconstrain( (sigmoid(inflection * ((t) - 0.5)) - error) / (1 - 2 * error) , 0 , 1)


def truncate_decimal(num):
    truncated_num = floor(num * 10) / 10
    return truncated_num


class Scene1(Scene):
    def construct(self):
        title = Text("Derivatives" , color=BLUE).scale(0.8)
        ans = Tex("It measures the " , "Instantaneous rate of Change" , " of a function!").scale(0.8)
        ans[1].set_color(YELLOW)

        self.wait()
        self.play(Write(title))
        self.wait()
        self.play(Write(ans) , title.animate.to_edge(UP))
        self.play(FadeOut(ans[0]) , FadeOut(ans[2]) , ans[1].animate.move_to(ORIGIN))
        self.wait()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        

class Scene2(Scene):
    def construct(self):
        carImage = ImageMobject("./car.png").scale(0.04)
        line = Line(start=LEFT * 4.5 , end=RIGHT * 4.5 , stroke_width=2 , color=RED).next_to(carImage , DOWN , buff=0)
        lineBrace = Brace(line , DOWN)
        brace_value = MathTex(r"50\;m").scale(0.6).next_to(lineBrace , DOWN)
        timetext = MathTex(r"\text{Time:}\;0.0s").scale(0.7).shift(UP *1.75)

        self.wait()
        self.play(FadeIn(carImage))
        self.play(
            carImage.animate.shift(LEFT * 4.5),
            Create(line),
            FadeIn(lineBrace , scale=0.7),
            Write(brace_value),
            FadeIn(timetext)
            )
        
        self.wait()


class Scene3_1(Scene):
    def construct(self):
        carImage = ImageMobject("./car.png").scale(0.04)
        line = Line(start=LEFT * 4.5 , end=RIGHT * 4.5 , stroke_width=2 , color=RED).next_to(carImage , DOWN , buff=0)
        lineBrace = Brace(line , DOWN)
        brace_value = MathTex(r"50\;m").scale(0.6).next_to(lineBrace , DOWN)
        carImage.shift(LEFT * 4.5)
        self.add(*[carImage , line , lineBrace , brace_value])

        self.wait()
        self.play(carImage.animate.shift(RIGHT * 9) , rate_func = mySmooth , run_time=5)
        self.wait()

class Scene3_2(Scene):
    def construct(self):
        time = ValueTracker(0)
        timetext = always_redraw(lambda: MathTex(r"\text{Time:}\;" , f"{truncate_decimal(time.get_value())}s").scale(0.7).shift(UP *1.75) )

        self.add(timetext)
        self.wait()
        self.play(time.animate.set_value(5) , rate_func = linear , run_time = 5)
        self.wait()


class Scene3_3(Scene):
    def construct(self):
        # a1 = Text("\"Instantaneous Rate of Change\"" , color = BLUE , t2c={"Instantaneous " : RED}).scale(0.7).shift(DOWN * 2)
        # a2 = Text("\"Instantaneous Rate of Change of Position\"" , color = BLUE , t2c={"Instantaneous " : RED}).scale(0.7).shift(DOWN * 2)
        # a3 = Text("\"Instantaneous Velocity\"" , color = BLUE , t2c={"Instantaneous " : RED}).scale(0.7).shift(DOWN * 2)


        a1 = Tex("Instantaneous " , "Rate of Change" , color = BLUE ).scale(0.9).shift(DOWN * 2)
        a2 = Tex("Instantaneous " , "Rate of Change of Position" , color = BLUE).scale(0.9).shift(DOWN * 2)
        a3 = Tex("Instantaneous " , "Velocity" , color = BLUE).scale(0.9).shift(DOWN * 2)
        a1[0].set_color(RED)
        a2[0].set_color(RED)
        a3[0].set_color(RED)

        self.wait()
        self.play(Write(a1))
        self.wait()
        self.play(TransformMatchingTex(a1 , a2))
        self.wait()
        self.play(TransformMatchingTex(a2 , a3))
        self.wait()

class Scene4(Scene):
    def construct(self):
        cloud = ArcPolygon(*[[-3,2,0] , [3,2,0] , [3,-2,0] , [-3,-2,0]] , arc_config=[
            {'radius':-4.25},
            {'radius':-2},
            {'radius':-4.25},
            {'radius':-2}
        ])
        dot1 = Circle(radius=0.1 , stroke_color=WHITE , stroke_width=2).move_to([4.7,-3.2,0])
        dot2 = Circle(radius=0.3 , stroke_color=WHITE , stroke_width=2.5).move_to([3.4,-2.9,0])
        instantaneous_vel = Text("\"Instantaneous velocity\"" , color=RED).scale(0.6).shift(UP * 2.1)
        moment = ImageMobject('./Scene3_Moment.jpg').scale(0.52).shift(LEFT * 2.25)
        formula = MathTex(r"velocity(v) = " , r"{Distance" , r"\over" ,  r"Time\;taken}" , color=BLUE).scale(0.7).shift(RIGHT * 2)
        formula[1].set_color(RED)
        formula[2].set_color(BLUE)
        formula[3].set_color(WHITE)

        formula2 = MathTex(r"velocity(v) = " , r"{Distance" , r"\over" ,  r"0}" , color=BLUE).scale(0.7).align_to(formula , LEFT)
        formula2[1].set_color(RED)
        formula2[2].set_color(BLUE)
        formula2[3].set_color(WHITE)

        formula3 = MathTex(r"velocity(v) = " , r"{0" , r"\over" ,  r"0}" , color=BLUE).scale(0.7).align_to(formula , LEFT)
        formula3[1].set_color(RED)
        formula3[2].set_color(BLUE)
        formula3[3].set_color(WHITE)
        # self.play(FadeIn(dot1 , scale=1.25) , run_time=0.35)
        # self.play(FadeIn(dot2 , scale=1.25) , run_time = 0.35)
        # self.play(FadeIn(cloud , scale=1.05) , run_time = 0.35)

        animations = [
            FadeIn(dot1 , scale=1.25 , run_time = 0.45),
            FadeIn(dot2 , scale=1.25 , run_time = 0.45),
            FadeIn(cloud , scale=1.05 , run_time = 0.45)
        ]

        self.play(AnimationGroup(*animations , lag_ratio=0.6))
        self.play(Write(instantaneous_vel) , run_time = 1)
        self.play(FadeIn(moment) , run_time = 0.3)
        self.play(Write(formula[0]))
        self.play(Write(formula[1]))
        self.play(Write(formula[2]) , run_time = 0.2)
        self.play(Write(formula[3]))
        self.play(TransformMatchingTex(formula , formula2))
        self.play(TransformMatchingTex(formula2 , formula3))
        self.wait()
        self.play(*[FadeOut(mob)for mob in self.mobjects])

class Scene5(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1 , 6 , 1],
            x_length=7,
            y_range=[-10 , 60 , 10],
            y_length=7,
            axis_config={'include_tip':True , 'include_numbers':True , 'font_size':20 ,'line_to_number_buff':0.17, 'tip_height':0.2 , 'tip_width':0.2,
                         'numbers_to_exclude':[-10 , -1]
                         }
        ).add_coordinates()
        labels = axes.get_axis_labels(
            Tex("Time(Sec)").scale(0.5), Tex("Distance(m)" , color=RED).scale(0.5)
        )
        carimage = ImageMobject("./car.png").scale(0.037).rotate(PI/2).move_to(axes.coords_to_point(-0.9,0))
        positionCurve = axes.plot(positionFunction , x_range=[0 , 5] , color=RED)
        time = ValueTracker(0)
        dot = always_redraw(lambda: Dot(axes.coords_to_point(time.get_value() , positionFunction(time.get_value()))) )
        lines = always_redraw(lambda: axes.get_lines_to_point(axes.c2p(time.get_value(), positionFunction(time.get_value())) , color=RED))
        soft = MathTex(r"s(" , r"t" , r")" , color= RED).scale(0.49).move_to(axes.coords_to_point(4.8 , 52))
        soft[1].set_color(WHITE)

        self.play(Create(axes))
        self.play(AnimationGroup(Write(labels[1]) , Write(labels[0]) , lag_ratio=0.9))
        self.play(FadeIn(carimage) , FadeIn(dot) , FadeIn(lines))
        self.play(
            carimage.animate(rate_func = mySmooth).shift(UP * 5),
            Create(positionCurve , rate_func = linear),
            time.animate(rate_func = linear).set_value(5),
            run_time=5
        )
        self.play(FadeOut(carimage) , FadeOut(dot) , FadeOut(lines))
        self.play(Write(soft))


        self.wait()

class Scene6(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1 , 6 , 1],
            x_length=7,
            y_range=[-10 , 60 , 10],
            y_length=7,
            axis_config={'include_tip':True , 'include_numbers':True , 'font_size':20 ,'line_to_number_buff':0.17, 'tip_height':0.2 , 'tip_width':0.2,
                         'numbers_to_exclude':[-10 , -1]
                         }
        ).add_coordinates()
        labels = axes.get_axis_labels(
            Tex("Time(Sec)").scale(0.5), Tex("Distance(m)" , color=RED).scale(0.5)
        )
        positionCurve = axes.plot(positionFunction , x_range=[0 , 5] , color=RED)
        soft = MathTex(r"s(" , r"t" , r")" , color= RED).scale(0.49).move_to(axes.coords_to_point(4.8 , 52))
        soft[1].set_color(WHITE)
        pointOn3 = Dot(axes.coords_to_point(3,0))
        sof3 = DashedLine(start=pointOn3.get_center() , end=axes.coords_to_point(3 , positionFunction(3)) , color=RED_B , stroke_width=2)
        sof3text = MathTex(r"s(" , r"3" , f")" , "=" , "38.92" , color = GOLD).scale(0.6).move_to(axes.coords_to_point(4 , 30))
        sof3text[1].set_color(WHITE)
        sof3text[3].set_color(WHITE)

        self.add(axes , labels , positionCurve , soft)


        self.play(FocusOn(pointOn3) , FadeIn(pointOn3) , run_time = 1)
        self.wait(0.5)
        self.play(Create(sof3) , run_time = 0.7)

        
        self.play(AnimationGroup(*[
            FadeIn (VGroup(sof3text[0] , sof3text[2]) ),
            FadeIn (VGroup(sof3text[1]) ),
            FadeIn (VGroup(sof3text[3]) ),
            FadeIn (VGroup(sof3text[4]) )
        ] , lag_ratio=0.7))

        self.wait()
        self.play(FadeOut(pointOn3 , sof3 , sof3text))



class Scene7(Scene):
    def construct(self):
        axes = Axes(
        x_range=[-1 , 6 , 1],
        x_length=7,
        y_range=[-10 , 60 , 10],
        y_length=7,
        axis_config={'include_tip':True , 'include_numbers':True , 'font_size':20 ,'line_to_number_buff':0.17, 'tip_height':0.2 , 'tip_width':0.2,
                        'numbers_to_exclude':[-10 , -1]
                        }
        ).add_coordinates()
        labels = axes.get_axis_labels(
            Tex("Time(Sec)").scale(0.5), Tex("Distance(m)" , color=RED).scale(0.5)
        )
        positionCurve = axes.plot(positionFunction , x_range=[0 , 5] , color=RED)
        soft = MathTex(r"s(" , r"t" , r")" , color= RED).scale(0.49).move_to(axes.coords_to_point(4.8 , 52))
        soft[1].set_color(WHITE)
        velocityCurve = axes.plot(velocityFunction , x_range=[0 , 5] , color=BLUE)
        voft = MathTex(r"v(" , r"t" , r")" , color= BLUE).scale(0.49).move_to(axes.coords_to_point(4.7 , 2))
        voft[1].set_color(WHITE)
        pointOn3 = Dot(axes.coords_to_point(3,0))
        vof3 = DashedLine(start=pointOn3.get_center() , end=axes.coords_to_point(3 , velocityFunction(3)) , color=BLUE_B , stroke_width=2)
        vof3text = MathTex(r"v(" , r"3" , f")" , "=" , "23.93(m/s)" , color = GOLD).scale(0.6).move_to(axes.coords_to_point(4.3 , 25))
        vof3text[1].set_color(WHITE)
        vof3text[3].set_color(WHITE)


        self.add(axes , labels , positionCurve , soft)
        self.play(Create(velocityCurve) , rate_func = linear , run_time=1.4)
        self.play(Write(voft))

        self.play(FocusOn(pointOn3) , FadeIn(pointOn3) , run_time = 1)
        self.wait(0.5)
        self.play(Create(vof3) , run_time = 0.7)

        
        self.play(AnimationGroup(*[
            FadeIn (VGroup(vof3text[0] , vof3text[2]) ),
            FadeIn (VGroup(vof3text[1]) ),
            FadeIn (VGroup(vof3text[3]) ),
            FadeIn (VGroup(vof3text[4]) )
        ] , lag_ratio=0.7))

        self.wait()
        self.play(FadeOut(pointOn3 , vof3 , vof3text))
        self.wait()

        velocityCurve2 = axes.plot(velocityFunction , x_range=[0 , 5] , color=BLUE , stroke_opacity=0.1)
        voft2 = MathTex(r"v(" , r"t" , r")" , color= BLUE).scale(0.49).move_to(axes.coords_to_point(4.7 , 2))
        voft2[1].set_color(WHITE)
        voft2.set_opacity(0.1)

        self.play(FadeTransform(velocityCurve , velocityCurve2) , FadeTransform(voft , voft2))



class Scene8(Scene):
    def construct(self):
        axes = Axes(
        x_range=[-1 , 6 , 1],
        x_length=7,
        y_range=[-10 , 60 , 10],
        y_length=7,
        axis_config={'include_tip':True , 'include_numbers':True , 'font_size':20 ,'line_to_number_buff':0.17, 'tip_height':0.2 , 'tip_width':0.2,
                        'numbers_to_exclude':[-10 , -1]
                        }
        ).add_coordinates()
        labels = axes.get_axis_labels(
            Tex("Time(Sec)").scale(0.5), Tex("Distance(m)" , color=RED).scale(0.5)
        )
        positionCurve = axes.plot(positionFunction , x_range=[0 , 5] , color=RED)
        soft = MathTex(r"s(" , r"t" , r")" , color= RED).scale(0.49).move_to(axes.coords_to_point(4.8 , 52))
        soft[1].set_color(WHITE)
        velocityCurve = axes.plot(velocityFunction , x_range=[0 , 5] , color=BLUE , stroke_opacity=0.1)
        voft = MathTex(r"v(" , r"t" , r")" , color= BLUE).scale(0.49).move_to(axes.coords_to_point(4.7 , 2))
        voft[1].set_color(WHITE)
        voft.set_opacity(0.1)


        positionCurve2 = axes.plot(positionFunction , x_range=[0 , 5] , color=RED , stroke_opacity=0.1)
        soft2 = MathTex(r"s(" , r"t" , r")" , color= RED).scale(0.49).move_to(axes.coords_to_point(4.8 , 52))
        soft2[1].set_color(WHITE)
        soft2.set_opacity(0.1)


        dottedline1 = DashedLine(start = axes.coords_to_point(3.4 , 0) , end=axes.coords_to_point(3.4 , 60) , color=YELLOW , stroke_width=1).set_opacity(0.6)
        dottedline2 = DashedLine(start = axes.coords_to_point(3.4 , 0) , end=axes.coords_to_point(3.4 , 60) , color=YELLOW , stroke_width=1).set_opacity(0.6)
        tracker1 = ValueTracker(3.4)
        tracker2 = ValueTracker(3.4)

        point1 = always_redraw(lambda: Dot(axes.coords_to_point(tracker1.get_value() , positionFunction(tracker1.get_value())) , color=WHITE , radius=0.05))
        point2 = always_redraw(lambda: Dot(axes.coords_to_point(tracker2.get_value() , positionFunction(tracker2.get_value())) , color=WHITE , radius=0.05))
        Vline = Line(start=axes.coords_to_point(3.8 , positionFunction(3.8)) , end=axes.coords_to_point(3.8 , positionFunction(3)) , stroke_width=2)
        Hline = Line(start=axes.coords_to_point(3 , positionFunction(3)) , end=axes.coords_to_point(3.8 , positionFunction(3)) , stroke_width=2)

        interval = Rectangle(stroke_width = 0 , height=6 , width=0.8 , fill_color=YELLOW_E , fill_opacity=0.45).shift(RIGHT * 0.9 + UP * 0.5)

        slopeline = Line(start=axes.coords_to_point(1 , 15.657) , end=axes.coords_to_point(4.74 , 59.156) , color=BLUE , stroke_width=2)


        self.add(axes , labels , positionCurve , soft , velocityCurve , voft)
        self.wait()

        self.play(FadeIn(dottedline1 , dottedline2 , point1 , point2) , run_time = 0.6)
        self.play(FadeIn(interval , scale=[0 , 1 , 0]) , dottedline1.animate.shift(LEFT * 0.4) , dottedline2.animate.shift(RIGHT * 0.4) , tracker1.animate.set_value(3) , tracker2.animate.set_value(3.8))
        self.play(AnimationGroup(*[Create(Vline) , Create(Hline)] , lag_ratio = 0.8))
        self.wait()

        self.play(AnimationGroup(*[Wiggle(Vline , scale_value=1.2 , rotation_angle=0.02*TAU) , Wiggle(Hline , scale_value=1.2, rotation_angle=0.02*TAU)] , lag_ratio = 0.7) , run_time=3)
        self.play(Create(slopeline))
        self.play(AnimationGroup(*[Indicate(labels[1] , scale_factor=1.3) , Indicate(labels[0] , scale_factor=1.3)] , lag_ratio=0.9) , run_time = 2)
        self.wait()
        self.play(FadeOut(interval, scale = [0 , 1 , 0]) , FadeOut(dottedline1 , shift = RIGHT * 0.4) , FadeOut(dottedline2 , shift = LEFT * 0.4) , FadeOut(slopeline , Hline , Vline) , FadeTransform(positionCurve , positionCurve2) , FadeTransform(soft , soft2) , tracker1.animate.set_value(3.4) , tracker2.animate.set_value(3.4))
        self.wait()


class Scene9(Scene):
    def construct(self):
        axes = Axes(
        x_range=[-1 , 6 , 1],
        x_length=7,
        y_range=[-10 , 60 , 10],
        y_length=7,
        axis_config={'include_tip':True , 'include_numbers':True , 'font_size':20 ,'line_to_number_buff':0.17, 'tip_height':0.2 , 'tip_width':0.2,
                        'numbers_to_exclude':[-10 , -1]
                        }
        ).add_coordinates()
        labels = axes.get_axis_labels(
            Tex("Time(Sec)").scale(0.5), Tex("Distance(m)" , color=RED).scale(0.5)
        )
        positionCurve = axes.plot(positionFunction , x_range=[0 , 5] , color=RED)
        soft = MathTex(r"s(" , r"t" , r")" , color= RED).scale(0.49).move_to(axes.coords_to_point(4.8 , 52))
        soft[1].set_color(WHITE)
        velocityCurve = axes.plot(velocityFunction , x_range=[0 , 5] , color=BLUE , stroke_opacity=0.1)
        voft = MathTex(r"v(" , r"t" , r")" , color= BLUE).scale(0.49).move_to(axes.coords_to_point(4.7 , 2))
        voft[1].set_color(WHITE)
        voft.set_opacity(0.1)


        positionCurve2 = axes.plot(positionFunction , x_range=[0 , 5] , color=RED , stroke_opacity=0.1)
        soft2 = MathTex(r"s(" , r"t" , r")" , color= RED).scale(0.49).move_to(axes.coords_to_point(4.8 , 52))
        soft2[1].set_color(WHITE)
        soft2.set_opacity(0.1)
        point = Dot(axes.coords_to_point(3.4 , positionFunction(3.4)) , color=WHITE , radius=0.05)

        path1 = axes.plot(positionFunction , x_range=[3.1 , 3.4] , color=RED).reverse_points()
        path2 = axes.plot(positionFunction , x_range=[3.4 , 3.8] , color=RED)

        text1 = Text("Then how does the derivative" , color=BLUE).shift(UP * 0.5)
        text2 = Text("solve the problem?" , color = BLUE).shift(DOWN * 0.5)
        canvas = Rectangle(color=BLACK , height = 3 , width = 7).set_opacity(0.6)




        self.add(axes , labels , positionCurve2 , soft2 , velocityCurve , voft , point)
        self.wait()

        self.bring_to_back(path1)
        self.bring_to_back(path2)
        self.play(Create(path1) , Create(path2))
        self.wait()
        self.play(FadeIn(canvas) , Write(text1))
        self.play(Write(text2))
        self.wait()


        nowStuff = VGroup(axes , labels , positionCurve2 , soft2 , velocityCurve , voft , point , path1 , path2 , canvas , text1 , text2)



        carImage = ImageMobject("./car.png").scale(0.04)
        line = Line(start=LEFT * 4.5 , end=RIGHT * 4.5 , stroke_width=2 , color=RED).next_to(carImage , DOWN , buff=0)
        lineBrace = Brace(line , DOWN)
        brace_value = MathTex(r"50\;m").scale(0.6).next_to(lineBrace , DOWN)
        timetext = MathTex(r"\text{Time:}\;0.0s").scale(0.7).shift(UP *1.75)
        carImage.shift(LEFT * 4.5)

        previousStuff = Group(carImage , line , lineBrace , brace_value , timetext)
        previousStuff.shift(UP * 8)


        self.add(previousStuff)
        self.play(nowStuff.animate.shift(DOWN * 8) , previousStuff.animate.shift(DOWN * 8) )
        self.wait()


class Scene10(Scene):
    def construct(self):
        carImage = ImageMobject("./car.png").scale(0.04)
        line = Line(start=LEFT * 4.5 , end=RIGHT * 4.5 , stroke_width=2 , color=RED).next_to(carImage , DOWN , buff=0)
        lineBrace = Brace(line , DOWN)
        brace_value = MathTex(r"50\;m").scale(0.6).next_to(lineBrace , DOWN)
        time = ValueTracker(0)
        timetext = always_redraw(lambda: MathTex(r"\text{Time:}\;" , f"{truncate_decimal(time.get_value())}s").scale(0.7).shift(UP *1.75) )
        carImage.shift(LEFT * 4.5)

        previousStuff = Group(carImage , line , lineBrace , brace_value , timetext)

        speedometer = Speedometer().scale(0.8).move_to([-4.5 , 1.8 , 0])
        pointer = always_redraw(lambda: Triangle(stroke_width = 0, fill_color = WHITE ,fill_opacity=1, stroke_color = WHITE).scale([0.036 , 1 , 0]).scale(0.8).rotate_about_origin((PI/2) + (30 * DEGREES)).move_to([-4.9,1.239,0]).rotate(velocityFunction(time.get_value()) * -3 * DEGREES,about_point=speedometer[3].get_center()) )

        speedometerText = Text("Speedometer:" , color=GREEN).scale(0.5).next_to(speedometer , UP)

        self.add(previousStuff)

        self.play(Write(speedometerText) , Create(speedometer) , DrawBorderThenFill(pointer))

        self.play(carImage.animate(rate_func=mySmooth).shift(RIGHT * 9) , time.animate(rate_func = linear).set_value(5) , run_time=7)

        self.wait()



class Scene11(Scene):
    def construct(self):
        carImage = ImageMobject("./car.png").scale(0.04)
        line = Line(start=LEFT * 4.5 , end=RIGHT * 4.5 , stroke_width=2 , color=RED).next_to(carImage , DOWN , buff=0)
        lineBrace = Brace(line , DOWN)
        brace_value = MathTex(r"50\;m").scale(0.6).next_to(lineBrace , DOWN)
        timetext = MathTex(r"\text{Time:}\;" , f"{truncate_decimal(5.0)}s").scale(0.7).shift(UP *1.75) 
        carImage.shift(RIGHT * 4.5)
        speedometer = Speedometer().scale(0.8).move_to([-4.5 , 1.8 , 0])
        pointer = (Triangle(stroke_width = 0, fill_color = WHITE ,fill_opacity=1, stroke_color = WHITE).scale([0.036 , 1 , 0]).scale(0.8).rotate_about_origin((PI/2) + (30 * DEGREES)).move_to([-4.9,1.239,0]))
        speedometerText = Text("Speedometer:" , color=GREEN).scale(0.5).next_to(speedometer , UP)

        previousStuff = Group(carImage , line , lineBrace , brace_value , timetext , speedometer , pointer , speedometerText)


        #####  Now Stuff  #####
        axes = Axes(
        x_range=[-1 , 6 , 1],
        x_length=7,
        y_range=[-10 , 60 , 10],
        y_length=7,
        axis_config={'include_tip':True , 'include_numbers':True , 'font_size':20 ,'line_to_number_buff':0.17, 'tip_height':0.2 , 'tip_width':0.2,
                        'numbers_to_exclude':[-10 , -1]
                        }
        ).add_coordinates()
        labels = axes.get_axis_labels(
            Tex("Time(Sec)").scale(0.5), Tex("Distance(m)" , color=RED).scale(0.5)
        )
        positionCurve = axes.plot(positionFunction , x_range=[0 , 5] , color=RED , stroke_width=3.35)
        soft = MathTex(r"s(" , r"t" , r")" , color= RED).scale(0.49).move_to(axes.coords_to_point(4.8 , 52))
        soft[1].set_color(WHITE)
        velocityCurve = axes.plot(velocityFunction , x_range=[0 , 5] , color=BLUE)
        voft = MathTex(r"v(" , r"t" , r")" , color= BLUE).scale(0.49).move_to(axes.coords_to_point(4.7 , 2))
        voft[1].set_color(WHITE)

        nowStuff = VGroup(axes , labels , positionCurve , soft).shift(DOWN * 8)

        self.add(previousStuff , nowStuff)
        self.wait()

        self.play(previousStuff.animate.shift(UP * 8) , nowStuff.animate.shift(UP * 8))

        point = Dot(axes.coords_to_point(2,0) , radius = 0.04)
        height = DashedLine(start=axes.coords_to_point(2,0) , end = axes.coords_to_point(2 , positionFunction(2)) , stroke_width=1.5 , dashed_ratio=0.5)
        pointoncurve = Dot(axes.coords_to_point(2 , positionFunction(2)) , color=RED , radius=0.03)

        interval = Line(start = axes.coords_to_point(2 , positionFunction(2)) , end = axes.coords_to_point(2.1 , positionFunction(2)) , stroke_width=1 , color=YELLOW)



        self.play(FadeIn(point) , FocusOn(point) , run_time = 0.7) 
        self.play(Create(height))
        self.play(FadeIn(pointoncurve) , run_time = 0.5)
        self.wait()
        self.play(Create(interval))
        self.wait()


class Scene12(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.15,
            zoomed_display_height=2.5,
            zoomed_display_width=2.5,
            image_frame_stroke_width=2,
            zoomed_camera_config={
                "default_frame_stroke_width": 2,
            },
            zoomed_camera_frame_starting_position=[-0.4,-1.3,0],
            **kwargs
        )


    def construct(self):
        # self.add(NumberPlane())




        axes = Axes(
        x_range=[-1 , 6 , 1],
        x_length=7,
        y_range=[-10 , 60 , 10],
        y_length=7,
        axis_config={'include_tip':True , 'include_numbers':True , 'font_size':20 ,'line_to_number_buff':0.17, 'tip_height':0.2 , 'tip_width':0.2,
                        'numbers_to_exclude':[-10 , -1]
                        }
        ).add_coordinates()
        labels = axes.get_axis_labels(
            Tex("Time(Sec)").scale(0.5), Tex("Distance(m)" , color=RED).scale(0.5)
        )
        positionCurve = axes.plot(positionFunction , x_range=[0 , 5] , color=RED , stroke_width=3.35)
        soft = MathTex(r"s(" , r"t" , r")" , color= RED).scale(0.49).move_to(axes.coords_to_point(4.8 , 52))
        soft[1].set_color(WHITE)
        point = Dot(axes.coords_to_point(2,0) , radius = 0.04)
        height = DashedLine(start=axes.coords_to_point(2,0) , end = axes.coords_to_point(2 , positionFunction(2)) , stroke_width=1.5 , dashed_ratio=0.5)
        pointoncurve = Dot(axes.coords_to_point(2 , positionFunction(2)) , color=RED , radius=0.03)

        interval = Line(start = axes.coords_to_point(2 , positionFunction(2)) , end = axes.coords_to_point(2.1 , positionFunction(2)) , stroke_width=0.7 , color=YELLOW)

        distanceTravelled = Line(start = axes.coords_to_point(2.1 , positionFunction(2)) , end = axes.coords_to_point(2.1 , positionFunction(2.1)) , stroke_width=0.7 , color=YELLOW)

        deltaS = MathTex(r"\Delta s" , color=RED).scale(0.093).next_to(distanceTravelled , RIGHT , buff=0.02)
        deltaT = MathTex(r"\Delta t" , color=WHITE).scale(0.084).next_to(interval , DOWN , buff=0.02)

        velocityeqn1 = MathTex(r"v(t)" , r"=" , r"{ \Delta s" , r"\over" , r"\Delta t }" , color=BLUE).scale(0.65).move_to(axes.coords_to_point(6 , 22))
        velocityeqn1[2].set_color(RED)
        velocityeqn1[4].set_color(WHITE)

        self.zoomed_camera.frame.move_to(axes.coords_to_point(2,positionFunction(2)) + [0.09 , 0.09 , 0]  )

        text = Text("Problem Solved!" , color=BLUE , font_size=50 , stroke_width=1 , stroke_color = WHITE)
        canvas = Rectangle(color=BLACK , height = 1.5 , width = 5).set_opacity(0.6)


        self.add(axes , labels, positionCurve , soft , point , height , pointoncurve , interval)

        self.activate_zooming(animate=True)
        self.wait()

        self.play(Indicate(interval, scale_factor = 1.35 , color=WHITE))
        self.wait()

        self.play(Create(distanceTravelled))

        self.play(FadeIn(deltaS))
        self.wait(0.3)
        self.play(FadeIn(deltaT))
        self.wait()

        self.play(Write(velocityeqn1))

        self.play(FadeIn(canvas) , Write(text))
        self.wait(2)

        self.play(FadeOut(canvas) , FadeOut(text))

        self.wait(1)


class Scene13(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.15,
            zoomed_display_height=2.5,
            zoomed_display_width=2.5,
            image_frame_stroke_width=2,
            zoomed_camera_config={
                "default_frame_stroke_width": 2,
            },
            zoomed_camera_frame_starting_position=[-0.4,-1.3,0],
            **kwargs
        )
    

    def construct(self):
        axes = Axes(
        x_range=[-1 , 6 , 1],
        x_length=7,
        y_range=[-10 , 60 , 10],
        y_length=7,
        axis_config={'include_tip':True , 'include_numbers':True , 'font_size':20 ,'line_to_number_buff':0.17, 'tip_height':0.2 , 'tip_width':0.2,
                        'numbers_to_exclude':[-10 , -1]
                        }
        ).add_coordinates()
        labels = axes.get_axis_labels(
            Tex("Time(Sec)").scale(0.5), Tex("Distance(m)" , color=RED).scale(0.5)
        )
        positionCurve = axes.plot(positionFunction , x_range=[0 , 5] , color=RED , stroke_width=3.35)
        soft = MathTex(r"s(" , r"t" , r")" , color= RED).scale(0.49).move_to(axes.coords_to_point(4.8 , 52))
        soft[1].set_color(WHITE)

        time = ValueTracker(2)
        always_redraw(lambda: self.zoomed_camera.frame.move_to(axes.coords_to_point(time.get_value(),positionFunction(time.get_value())) + [0.09 , 0.09 , 0]  ) )

        point = always_redraw(lambda: Dot(axes.coords_to_point(time.get_value(),0) , radius = 0.04) )
        height = always_redraw(lambda: DashedLine(start=axes.coords_to_point(time.get_value(),0) , end = axes.coords_to_point(time.get_value() , positionFunction(time.get_value())) , stroke_width=1.5 , dashed_ratio=0.5) )
        pointoncurve = always_redraw(lambda: Dot(axes.coords_to_point(time.get_value() , positionFunction(time.get_value())) , color=RED , radius=0.03))

        interval = always_redraw(lambda: Line(start = axes.coords_to_point(time.get_value() , positionFunction(time.get_value())) , end = axes.coords_to_point(time.get_value() + 0.1 , positionFunction(time.get_value())) , stroke_width=0.7 , color=YELLOW))

        distanceTravelled = always_redraw(lambda: Line(start = axes.coords_to_point(time.get_value()  + 0.1 , positionFunction(time.get_value())) , end = axes.coords_to_point(time.get_value() + 0.1 , positionFunction(time.get_value() + 0.1)) , stroke_width=0.7 , color=YELLOW) )

        deltaS = always_redraw(lambda: MathTex(r"\Delta s" , color=RED).scale(0.093).next_to(distanceTravelled , RIGHT , buff=0.02))
        deltaT = always_redraw(lambda: MathTex(r"\Delta t" , color=WHITE).scale(0.084).next_to(interval , DOWN , buff=0.02))

        velocityeqn1 = MathTex(r"v(t)" , r"=" , r"{ \Delta s" , r"\over" , r"\Delta t }" , color=BLUE).scale(0.65).move_to(axes.coords_to_point(6 , 22))
        velocityeqn1[2].set_color(RED)
        velocityeqn1[4].set_color(WHITE)

        self.activate_zooming(animate=False)
        self.add(axes , labels , positionCurve , soft , point , height , pointoncurve , interval , distanceTravelled , deltaS , deltaT , velocityeqn1)

        self.play(time.animate.set_value(1.5) , run_time = 1 , rate_func = ease_in_sine)
        self.wait()
        self.play(time.animate.set_value(4) , run_time = 3.25 , rate_func = ease_in_sine)
        self.wait()
        self.play(time.animate.set_value(2))

        self.wait()



class Scene14(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.15,
            zoomed_display_height=2.5,
            zoomed_display_width=2.5,
            image_frame_stroke_width=2,
            zoomed_camera_config={
                "default_frame_stroke_width": 2,
            },
            zoomed_camera_frame_starting_position=[-0.4,-1.3,0],
            **kwargs
        )

    def construct(self):
        axes = Axes(
        x_range=[-1 , 6 , 1],
        x_length=7,
        y_range=[-10 , 60 , 10],
        y_length=7,
        axis_config={'include_tip':True , 'include_numbers':True , 'font_size':20 ,'line_to_number_buff':0.17, 'tip_height':0.2 , 'tip_width':0.2,
                        'numbers_to_exclude':[-10 , -1]
                        }
        ).add_coordinates()
        labels = axes.get_axis_labels(
            Tex("Time(Sec)").scale(0.5), Tex("Distance(m)" , color=RED).scale(0.5)
        )
        positionCurve = axes.plot(positionFunction , x_range=[0 , 5] , color=RED , stroke_width=3.35)
        soft = MathTex(r"s(" , r"t" , r")" , color= RED).scale(0.49).move_to(axes.coords_to_point(4.8 , 52))
        soft[1].set_color(WHITE)

        self.zoomed_camera.frame.move_to(axes.coords_to_point(2,positionFunction(2)) + [0.09 , 0.09 , 0]  ) 

        point = always_redraw(lambda: Dot(axes.coords_to_point(2,0) , radius = 0.04) )
        height = always_redraw(lambda: DashedLine(start=axes.coords_to_point(2,0) , end = axes.coords_to_point(2 , positionFunction(2)) , stroke_width=1.5 , dashed_ratio=0.5) )
        pointoncurve = always_redraw(lambda: Dot(axes.coords_to_point(2 , positionFunction(2)) , color=RED , radius=0.03))

        interval = always_redraw(lambda: Line(start = axes.coords_to_point(2 , positionFunction(2)) , end = axes.coords_to_point(2 + 0.1 , positionFunction(2)) , stroke_width=0.7 , color=YELLOW))

        distanceTravelled = always_redraw(lambda: Line(start = axes.coords_to_point(2  + 0.1 , positionFunction(2)) , end = axes.coords_to_point(2 + 0.1 , positionFunction(2 + 0.1)) , stroke_width=0.7 , color=YELLOW) )

        deltaS = always_redraw(lambda: MathTex(r"\Delta s" , color=RED).scale(0.093).next_to(distanceTravelled , RIGHT , buff=0.02))
        deltaT = always_redraw(lambda: MathTex(r"\Delta t" , color=WHITE).scale(0.084).next_to(interval , DOWN , buff=0.02))

        velocityeqn1 = MathTex(r"v(t)" , r"=" , r"{ \Delta s" , r"\over" , r"\Delta t }" , color=BLUE).scale(0.65).move_to(axes.coords_to_point(6 , 22))
        velocityeqn1[2].set_color(RED)
        velocityeqn1[4].set_color(WHITE)

        velocityeqn2 = MathTex(r"v(t)" , r"=" , r"{ s(t + \Delta t) - s(t)" , r"\over" , r"\Delta t }" , color=BLUE).scale(0.65).move_to(axes.coords_to_point(6 , 22)).align_to(velocityeqn1 , LEFT)
        velocityeqn2[2].set_color(RED)
        velocityeqn2[4].set_color(WHITE)

        velocityeqn3 = MathTex(r"v(t)" , r"\approx" , r"{ s(t + \Delta t) - s(t)" , r"\over" , r"\Delta t }" , color=BLUE).scale(0.65).move_to(axes.coords_to_point(6 , 22)).align_to(velocityeqn1 , LEFT)
        velocityeqn3[2].set_color(RED)
        velocityeqn3[4].set_color(WHITE)

        distance1 = Line(end = axes.coords_to_point(2  + 0.1 , positionFunction(2)) , start = axes.coords_to_point(2 + 0.1 , 0) , stroke_width=0.7 , color=YELLOW)
        brace1 = Brace(VGroup(distance1 , distanceTravelled) , RIGHT , buff=0.35 , sharpness=4)
        brace2 = Brace(distance1 , RIGHT , buff=0.09 , sharpness=4)

        self.activate_zooming(animate=False)
        self.add(axes , labels , positionCurve , soft , point , height , pointoncurve , interval , distanceTravelled , deltaS , deltaT , velocityeqn1)
        self.wait()

        self.play(FocusOn(axes.coords_to_point(2.1 , 0)))
        self.play(Create(distance1))
        self.play(FadeIn(brace1))
        self.play(FadeIn(brace2))
        self.play(TransformMatchingTex(velocityeqn1 , velocityeqn2))
        self.wait()

        self.play(FadeOut(brace1 , brace2))
        
        self.play(TransformMatchingTex(velocityeqn2 , velocityeqn3))
        self.wait()

class Scene15(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.15,
            zoomed_display_height=2.5,
            zoomed_display_width=2.5,
            image_frame_stroke_width=2,
            zoomed_camera_config={
                "default_frame_stroke_width": 2,
            },
            zoomed_camera_frame_starting_position=[-0.4,-1.3,0],
            **kwargs
        )

    def construct(self):
        axes = Axes(
        x_range=[-1 , 6 , 1],
        x_length=7,
        y_range=[-10 , 60 , 10],
        y_length=7,
        axis_config={'include_tip':True , 'include_numbers':True , 'font_size':20 ,'line_to_number_buff':0.17, 'tip_height':0.2 , 'tip_width':0.2,
                        'numbers_to_exclude':[-10 , -1]
                        }
        ).add_coordinates()
        labels = axes.get_axis_labels(
            Tex("Time(Sec)").scale(0.5), Tex("Distance(m)" , color=RED).scale(0.5)
        )
        positionCurve = axes.plot(positionFunction , x_range=[0 , 5] , color=RED , stroke_width=3.35)
        soft = MathTex(r"s(" , r"t" , r")" , color= RED).scale(0.49).move_to(axes.coords_to_point(4.8 , 52))
        soft[1].set_color(WHITE)

        self.zoomed_camera.frame.move_to(axes.coords_to_point(2,positionFunction(2)) + [0.09 , 0.09 , 0]  ) 

        point = always_redraw(lambda: Dot(axes.coords_to_point(2,0) , radius = 0.04) )
        height = always_redraw(lambda: DashedLine(start=axes.coords_to_point(2,0) , end = axes.coords_to_point(2 , positionFunction(2)) , stroke_width=1.5 , dashed_ratio=0.5) )
        pointoncurve = always_redraw(lambda: Dot(axes.coords_to_point(2 , positionFunction(2)) , color=RED , radius=0.03))

        intervalLength = ValueTracker(0.1)
        interval = always_redraw(lambda: Line(start = axes.coords_to_point(2 , positionFunction(2)) , end = axes.coords_to_point(2 + intervalLength.get_value() , positionFunction(2)) , stroke_width=0.7 , color=YELLOW))

        distanceTravelled = always_redraw(lambda: Line(start = axes.coords_to_point(2  + intervalLength.get_value() , positionFunction(2)) , end = axes.coords_to_point(2 + intervalLength.get_value() , positionFunction(2 + intervalLength.get_value())) , stroke_width=0.7 , color=YELLOW) )

        deltaS = always_redraw(lambda: MathTex(r"\Delta s" , color=RED).scale(0.093).next_to(distanceTravelled , RIGHT , buff=0.02))
        deltaT = always_redraw(lambda: MathTex(r"\Delta t" , color=WHITE).scale(0.084).next_to(interval , DOWN , buff=0.02))



        velocityeqn1 = MathTex(r"v(t)" , r"=" , r"{ \Delta s" , r"\over" , r"\Delta t }" , color=BLUE).scale(0.65).move_to(axes.coords_to_point(6 , 22))
        velocityeqn1[2].set_color(RED)
        velocityeqn1[4].set_color(WHITE)

        velocityeqn = MathTex(r"v(t)" , r"\approx" , r"{ s(t + \Delta t) - s(t)" , r"\over" , r"\Delta t }" , color=BLUE).scale(0.65).move_to(axes.coords_to_point(6 , 22)).align_to(velocityeqn1 , LEFT)
        velocityeqn[2].set_color(RED)
        velocityeqn[4].set_color(WHITE)

        derivativeeqn = MathTex(r"{ds \over dt}" , r"/v(t)" , r"=" , r"\lim_{\Delta t \to 0}" , r"{ \Delta s" , r"\over" , r"\Delta t}" , color=BLUE).scale(0.65).next_to(velocityeqn , RIGHT , buff=1)
        derivativeeqn[3].set_color(WHITE)
        derivativeeqn[4].set_color(RED)
        derivativeeqn[6].set_color(WHITE)

        derivativeeqn2 = MathTex(r"{ds \over dt}" , r"/v(t)" , r"=" , r"\lim_{ \Delta t \to 0}" , r"{ s(t + \Delta t) - s(t)" , r"\over" , r"\Delta t }" , color=BLUE).scale(0.65).next_to(derivativeeqn , DOWN , buff=0.55).align_to(derivativeeqn , LEFT)
        derivativeeqn2[3].set_color(WHITE)
        derivativeeqn2[4].set_color(RED)
        derivativeeqn2[6].set_color(WHITE)


        distance1 = Line(end = axes.coords_to_point(2  + intervalLength.get_value() , positionFunction(2)) , start = axes.coords_to_point(2 + intervalLength.get_value() , 0) , stroke_width=0.7 , color=YELLOW)


        self.activate_zooming(animate=False)
        self.add(axes , labels , positionCurve , soft , point , height , pointoncurve , interval , distanceTravelled , deltaS , deltaT , velocityeqn , distance1)
        self.wait()

        self.play(self.camera.frame.animate.shift(RIGHT * 9) , Write(derivativeeqn[0]))
        self.play(Write(derivativeeqn[1]))
        self.play(Write(derivativeeqn[2]))
        self.play(Write(VGroup(derivativeeqn[4] , derivativeeqn[5] , derivativeeqn[6])))
        self.play(Write(derivativeeqn[3]))

        self.play(Write(derivativeeqn2))
        self.wait()
        self.play(self.camera.frame.animate.shift(LEFT * 9)   , FadeOut(point , pointoncurve , interval , distanceTravelled , height , deltaT , deltaS , distance1) , FadeOut(self.zoomed_display) , FadeOut(self.zoomed_camera.frame))
        self.wait()


class Scene16(MovingCameraScene):
    def construct(self):
        # self.add(NumberPlane())

        axes = Axes(
        x_range=[-1 , 6 , 1],
        x_length=7,
        y_range=[-10 , 60 , 10],
        y_length=7,
        axis_config={'include_tip':True , 'include_numbers':True , 'font_size':20 ,'line_to_number_buff':0.17, 'tip_height':0.2 , 'tip_width':0.2,
                        'numbers_to_exclude':[-10 , -1]
                        }
        ).add_coordinates()
        labels = axes.get_axis_labels(
            Tex("Time(Sec)").scale(0.5), Tex("Distance(m)" , color=RED).scale(0.5)
        )
        positionCurve = axes.plot(positionFunction , x_range=[0 , 5] , color=RED , stroke_width=3.35)
        soft = MathTex(r"s(" , r"t" , r")" , color= RED).scale(0.49).move_to(axes.coords_to_point(4.8 , 52))
        soft[1].set_color(WHITE)




        velocityeqn1 = MathTex(r"v(t)" , r"=" , r"{ \Delta s" , r"\over" , r"\Delta t }" , color=BLUE).scale(0.65).move_to(axes.coords_to_point(6 , 22))
        velocityeqn1[2].set_color(RED)
        velocityeqn1[4].set_color(WHITE)

        velocityeqn = MathTex(r"v(t)" , r"\approx" , r"{ s(t + \Delta t) - s(t)" , r"\over" , r"\Delta t }" , color=BLUE).scale(0.65).move_to(axes.coords_to_point(6 , 22)).align_to(velocityeqn1 , LEFT)
        velocityeqn[2].set_color(RED)
        velocityeqn[4].set_color(WHITE)

        derivativeeqn = MathTex(r"{ds \over dt}" , r"/v(t)" , r"=" , r"\lim_{\Delta t \to 0}" , r"{ \Delta s" , r"\over" , r"\Delta t}" , color=BLUE).scale(0.65).next_to(velocityeqn , RIGHT , buff=1)
        derivativeeqn[3].set_color(WHITE)
        derivativeeqn[4].set_color(RED)
        derivativeeqn[6].set_color(WHITE)

        derivativeeqn2 = MathTex(r"{ds \over dt}" , r"/v(t)" , r"=" , r"\lim_{ \Delta t \to 0}" , r"{ s(t + \Delta t) - s(t)" , r"\over" , r"\Delta t }" , color=BLUE).scale(0.65).next_to(derivativeeqn , DOWN , buff=0.55).align_to(derivativeeqn , LEFT)
        derivativeeqn2[3].set_color(WHITE)
        derivativeeqn2[4].set_color(RED)
        derivativeeqn2[6].set_color(WHITE)


        interval = ValueTracker(1)
        time = 1.4
        secantLine = always_redraw(lambda: LineThroughPoints( axes.coords_to_point(time , positionFunction(time)) , axes.coords_to_point(time + interval.get_value() , positionFunction(time + interval.get_value())) , x_range=[-3 , 2] , stroke_width=2 , color=BLUE ))
        Vline = always_redraw(lambda: Line(start=axes.coords_to_point(time + interval.get_value() , positionFunction(time + interval.get_value())) , end = axes.coords_to_point(time + interval.get_value() , positionFunction(time)) , stroke_width=2) )
        Hline = always_redraw(lambda: Line(start=axes.coords_to_point(time , positionFunction(time)) , end = axes.coords_to_point(time + interval.get_value() , positionFunction(time)) , stroke_width=2) )

        deltas = always_redraw(lambda: MathTex(r"\Delta s", color=RED).scale(interval.get_value()/2).next_to(Vline , RIGHT , buff=interval.get_value()/10) )
        deltat = always_redraw(lambda: MathTex(r"\Delta t").scale(interval.get_value()/2).next_to(Hline , UP ,  buff=interval.get_value()/10) )

        velocityCurve = axes.plot(velocityFunction , x_range=[0 , 5] , color=BLUE , stroke_width=3.35)
        voft = MathTex(r"v(" , r"t" , r")" , color= BLUE).scale(0.49).move_to(axes.coords_to_point(4.7 , 2))
        voft[1].set_color(WHITE)

        velocityCurve2 = axes.plot(velocityFunction , x_range=[0 , 5] , color=BLUE , stroke_width=3.35 , stroke_opacity=0.1)
        voft2 = MathTex(r"v(" , r"t" , r")" , color= BLUE).scale(0.49).move_to(axes.coords_to_point(4.7 , 2))
        voft2[1].set_color(WHITE)
        voft2.set_opacity(0.1)

        tangentTracker = ValueTracker(0)
        verticalLine = always_redraw(lambda: Line(start=axes.coords_to_point(tangentTracker.get_value() , 0), end=axes.coords_to_point(tangentTracker.get_value() , positionFunction(tangentTracker.get_value())) , stroke_width=2))
        tangent = always_redraw(lambda: LineThroughPoints( axes.coords_to_point(tangentTracker.get_value() , positionFunction(tangentTracker.get_value())) , axes.coords_to_point(tangentTracker.get_value() + 0.001 , positionFunction(tangentTracker.get_value() + 0.001)) , line_length = 3, stroke_width=2 , color=GREEN ))

        pointTracker = ValueTracker(0)
        pointoncurve = always_redraw(lambda: Dot(axes.coords_to_point(pointTracker.get_value() , velocityFunction(pointTracker.get_value())) , radius=0.07))

        self.add(axes , labels , positionCurve , soft , velocityeqn , derivativeeqn , derivativeeqn2)
        self.wait()

        self.play(Create(secantLine) , Create(Hline) , Create(Vline) , Write(deltas) , Write(deltat))
        self.wait()

        self.play(interval.animate.set_value(0.001) , rate_func = linear , run_time = 4)
        self.wait(1.5)
        self.play(FadeOut(secantLine , deltas , deltat , Vline , Hline))

        self.play(AnimationGroup(Create(velocityCurve) , Write(voft) , lag_ratio=0.8))

        self.play(self.camera.frame.animate.shift(RIGHT * 3.85) , VGroup(velocityeqn , derivativeeqn , derivativeeqn2).animate.shift(LEFT))
        self.play(Indicate(derivativeeqn2 , scale_factor=1.3))
        self.wait()
        self.play(FadeTransform(velocityCurve , velocityCurve2) , FadeTransform(voft , voft2))
        self.wait()

        self.play(FadeIn(verticalLine , tangent))
        self.play(tangentTracker.animate.set_value(5) , run_time = 5.5 , rate_func = linear)        
        self.wait()
        self.play(FadeOut(tangent , verticalLine) , FadeTransform(velocityCurve2 , velocityCurve) , FadeTransform(voft2 , voft))

        self.play(FadeIn(pointoncurve) , FocusOn(pointoncurve) , run_time=1)
        self.wait()
        self.play(pointTracker.animate.set_value(2.5))
        self.wait()
        self.play(pointTracker.animate.set_value(5))
        self.wait()
        self.play(*[FadeOut(mob)for mob in self.mobjects])