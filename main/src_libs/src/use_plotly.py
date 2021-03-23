
import plotly.express as px
import plotly.graph_objects as go

def create_line_plot (data_frame= None, x=None, y=None, 
                line_group=None, color=None, 
                line_dash=None, hover_name=None, 
                hover_data=None, custom_data=None, 
                text=None, facet_row=None, facet_col=None, 
                facet_col_wrap=0, facet_row_spacing=None, 
                facet_col_spacing=None, error_x=None, 
                error_x_minus=None, error_y=None, 
                error_y_minus=None, animation_frame=None, 
                animation_group=None, category_orders=None, 
                labels=None, orientation=None, color_discrete_sequence=None, 
                color_discrete_map=None, line_dash_sequence=None, line_dash_map=None, 
                log_x=False, log_y=False, range_x=None, range_y=None, line_shape=None, 
                render_mode='auto', title=None, template=None, width=None, 
                height=None, save= False, path= 'Output/', name= None):
    """
                        ---What it does---
    This function creates a line plot. Then stores the plot in html format if desired.

                        ---What it needs---
        - Data to plot (data).
        - A save state for saving up your plots (save). Set to False by default
        - A ending path for your html to be stored (path). Set to /Output by default
        - The name of your plot (name)
        - The standard plotly express argument for this function

                        ---What it returns---
    This function does not return anything
    """
        
    fig = px.line(data_frame= data_frame, x=x, y= y,
                line_group= line_group, color= color, 
                line_dash= line_dash, hover_name= hover_name, 
                hover_data= hover_data, custom_data= custom_data, 
                text= text, facet_row= facet_row, facet_col= facet_col, 
                facet_col_wrap= facet_col_wrap, facet_row_spacing= facet_row_spacing, 
                facet_col_spacing= facet_col_spacing, error_x= error_x, 
                error_x_minus= error_x_minus, error_y= error_y, 
                error_y_minus= error_y_minus, animation_frame= animation_frame, 
                animation_group= animation_group, category_orders= category_orders, 
                labels= labels, orientation= orientation, 
                color_discrete_sequence=color_discrete_sequence, 
                color_discrete_map=color_discrete_map, line_dash_sequence=line_dash_sequence, 
                line_dash_map= line_dash_map, log_x= log_x, log_y= log_y, 
                range_x= range_x, range_y= range_y, line_shape= line_shape, 
                render_mode= render_mode, title= title, template= template, width= width, 
                height=height)
    fig.show()

    if save == True:
        full_path = f'{path}{name}.html' 
        fig.write_html(full_path)


def create_bar_plot(data_frame=None, x=None, y=None, 
                    color=None, facet_row=None, facet_col=None, 
                    facet_col_wrap=0, facet_row_spacing=None, 
                    facet_col_spacing=None, hover_name=None, 
                    hover_data=None, custom_data=None, text=None, 
                    base=None, error_x=None, error_x_minus=None, 
                    error_y=None, error_y_minus=None, animation_frame=None, 
                    animation_group=None, category_orders=None, 
                    labels=None, color_discrete_sequence=None, 
                    color_discrete_map=None, color_continuous_scale=None, 
                    range_color=None, color_continuous_midpoint=None, 
                    opacity=None, orientation=None, barmode='relative', 
                    log_x=False, log_y=False, range_x=None, range_y=None, 
                    title=None, template=None, width=None, height=None,
                    save= False, path= 'Output/', name= None):
    """
                        ---What it does---
    This function creates a bar plot. Then stores the plot in html format if desired.

                        ---What it needs---
        - Data to plot (data).
        - A save state for saving up your plots (save). Set to False by default
        - A ending path for your html to be stored (path). Set to /Output by default
        - The name of your plot (name)
        - The standard plotly express argument for this function

                        ---What it returns---
    This function does not return anything
    """
    
    fig = px.bar(data_frame= data_frame, x= x, y= y, 
                    color= color, facet_row= facet_row, facet_col= facet_col, 
                    facet_col_wrap= facet_col_wrap, facet_row_spacing= facet_row_spacing, 
                    facet_col_spacing= facet_col_spacing, hover_name= hover_name, 
                    hover_data= hover_data, custom_data= custom_data, text= text, 
                    base= base, error_x= error_x, error_x_minus= error_x_minus, 
                    error_y= error_y, error_y_minus= error_y_minus,
                    animation_frame= animation_frame, 
                    animation_group= animation_group, category_orders= category_orders, 
                    labels= labels, color_discrete_sequence= color_discrete_sequence, 
                    color_discrete_map= color_discrete_map, 
                    color_continuous_scale= color_continuous_scale, 
                    range_color= range_color, 
                    color_continuous_midpoint= color_continuous_midpoint, 
                    opacity= opacity, orientation= orientation, barmode= barmode, 
                    log_x= log_x, log_y= log_y, range_x= range_x, range_y= range_y, 
                    title= title, template= template, width= width, height= height)
    
    fig.show()

    if save == True:
        full_path = f'{path}{name}.html' 
        fig.write_html(full_path)


def create_pie_plot(data_frame=None, names=None, values=None, 
                    color=None, color_discrete_sequence=None, 
                    color_discrete_map=None, hover_name=None, 
                    hover_data=None, custom_data=None, labels=None, 
                    title=None, template=None, width=None, height=None, 
                    opacity=None, hole=None, save= False, path= 'Output/', 
                    name= None):
    """
                        ---What it does---
    This function creates a pie plot. Then stores the plot in html format if desired.

                        ---What it needs---
        - Data to plot (data).
        - A save state for saving up your plots (save). Set to False by default
        - A ending path for your html to be stored (path). Set to /Output by default
        - The name of your plot (name)
        - The standard plotly express argument for this function

                        ---What it returns---
    This function does not return anything
    """
        
    fig = px.pie(data_frame= data_frame, names= names, values= values, 
                    color= color, color_discrete_sequence= color_discrete_sequence, 
                    color_discrete_map= color_discrete_map, hover_name= hover_name, 
                    hover_data= hover_data, custom_data= custom_data, labels= labels, 
                    title= title, template= template, width= width, height= height, 
                    opacity= opacity, hole= hole)

    fig.show()

    if save == True:
        full_path = f'{path}{name}.html' 
        fig.write_html(full_path)


def create_heat_map(data = None, save= False, path= 'Output/', 
                    name= None):
    """
    TODO lack in function options
                        ---What it does---
    Creates a heat map plot selecting only numerical data.Then writes an htm file with the plot if desired.

                        ---What it needs---
        - Data to plot (data).
        - A save state for saving up your plots (save). Set to False by default
        - A ending path for your html to be stored (path). Set to /Output by default
        - The name of your plot (name)

                        ---What it returns---
    This function does not return anything
    """

    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    corr = data.select_dtypes(include= numerics).corr()

    fig = px.imshow(corr)
    fig.show()

    if save == True:
        full_path = f'{path}{name}.html' 
        fig.write_html(full_path)


def create_map():
    pass