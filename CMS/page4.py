import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
from Add_logo import add_logo



st.set_page_config(page_title='CMS Platform',  layout='wide', page_icon='assets/imgs/lvlAlpha_logo.png', 
                   initial_sidebar_state='expanded',
                   menu_items = {
                        'Report a Bug': "mailto:contact@lvlalpha.com",
                        'About' : "The App is powered by lvlAlpha Pvt. Ltd."
                   })

add_logo(logo_url = 'assets/imgs/ArmyLogo.png')

javascript_code = """
(function( $ ) {

    "use strict";

    function isTouchEnabled() {
        return (('ontouchstart' in window)
            || (navigator.MaxTouchPoints > 0)
            || (navigator.msMaxTouchPoints > 0));
    }

     $(document).ready(function () {
        $("path[id^=\"basic_\"]").each(function (i, e) {
            addEvent($(e).attr('id'));
        });
    });

    function addEvent(id, relationId) {
        var _obj = $('#' + id);
        $('#basic-wrapper').css({'opacity': '1'});

        _obj.attr({'fill': 'rgba(255, 0, 0, 0)', 'stroke': 'rgba(255, 102, 102, 1)'});
        _obj.attr({'cursor': 'default'});

        if (basic_config[id]['active'] === true) {
            if (isTouchEnabled()) {
                var touchmoved;
                _obj.on('touchend', function (e) {
                    if (touchmoved !== true) {
                        _obj.on('touchstart', function (e) {
                            let touch = e.originalEvent.touches[0];
                            let x = touch.pageX - 10, y = touch.pageY + (-15);

                            let $basicatip = $('#tip-basic');
                            let basicanatomytipw = $basicatip.outerWidth(),
                                basicanatomytiph = $basicatip.outerHeight();

                            x = (x + basicanatomytipw > $(document).scrollLeft() + $(window).width()) ? x - basicanatomytipw - (20 * 2) : x
                            y = (y + basicanatomytiph > $(document).scrollTop() + $(window).height()) ? $(document).scrollTop() + $(window).height() - basicanatomytiph - 10 : y

                            if (basic_config[id]['target'] !== 'none') {
                                _obj.css({'fill': 'rgba(255, 0, 0, 0.7)'});
                            }
                            $basicatip.show().html(basic_config[id]['hover']);
                            $basicatip.css({left: x, top: y})
                        })
                        _obj.on('touchend', function () {
                            _obj.css({'fill': 'rgba(255, 0, 0, 0)'});
                            if (basic_config[id]['target'] === '_blank') {
                                window.open(basic_config[id]['url']);
                            } else if (basic_config[id]['target'] === '_self') {
                                window.parent.location.href = basic_config[id]['url'];
                            }
                            $('#tip-basic').hide();
                        })
                    }
                }).on('touchmove', function (e) {
                    touchmoved = true;
                }).on('touchstart', function () {
                    touchmoved = false;
                });
            }
            _obj.attr({'cursor': 'pointer'});

            _obj.on('mouseenter', function () {
                $('#tip-basic').show().html(basic_config[id]['hover']);
                _obj.css({'fill': 'rgba(255, 0, 0, 0.3)'})
            }).on('mouseleave', function () {
                $('#tip-basic').hide();
                _obj.css({'fill': 'rgba(255, 0, 0, 0)'});
            })
            if (basic_config[id]['target'] !== 'none') {
                _obj.on('mousedown', function () {
                    _obj.css({'fill': 'rgba(255, 0, 0, 0.7)'});
                })
            }
            _obj.on('mouseup', function () {
                _obj.css({'fill': 'rgba(255, 0, 0, 0.3)'});
                if (basic_config[id]['target'] === '_blank') {
                    window.open(basic_config[id]['url']);
                } else if (basic_config[id]['target'] === '_self') {
                    window.parent.location.href = basic_config[id]['url'];
                }
            })
            _obj.on('mousemove', function (e) {
                let x = e.pageX + 10, y = e.pageY + 15;

                let $abasic = $('#tip-basic');
                let basicanatomytipw = $abasic.outerWidth(), basicanatomytiph = $abasic.outerHeight();

                x = (x + basicanatomytipw > $(document).scrollLeft() +
                    $(window).width()) ? x - basicanatomytipw - (20 * 2) : x
                y = (y + basicanatomytiph > $(document).scrollTop() + $(window).height()) ?
                    $(document).scrollTop() + $(window).height() - basicanatomytiph - 10 : y

                $abasic.css({left: x, top: y})
            })
        } else {
            _obj.hide();
        }
    }
})(jQuery);

})(jQuery);
"""
jquery_code = '<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>'
st.components.v1.html(jquery_code)
st.components.v1.html(javascript_code)

st.title("Injury Report")

with st.container():
    # st.header("Body Layers")
    selectCanvas = st.radio("Body Layer",
                            options = ('Skin', 'Muscular', 'Skeleton', 'Nervous'),
                            horizontal = True,
                            label_visibility = 'hidden')

    if selectCanvas == 'Skin':
        fbody_canvas = st_canvas(
            stroke_width = 3,
            background_image = Image.open("assets/imgs/Skin_Body.png"),
            height = 720,
            width = 1050,
            key = "Skin"
        )
    elif selectCanvas == 'Muscular':
        fbody_canvas = st_canvas(
            stroke_width = 3,
            background_image = Image.open("assets/imgs/Muscle_Body.png"),
            height = 720,
            width = 1050,
            key = "Muscular"
        )
    elif selectCanvas == 'Skeleton':
        fbody_canvas = st_canvas(
            stroke_width = 3,
            background_image = Image.open("assets/imgs/Skeleton_Body.png"),
            height = 720,
            width = 1050,
            key = "Skeleton"
        )
    else:
        fbody_canvas = st_canvas(
            stroke_width = 3,
            background_image = Image.open("assets/imgs/Nerve_Body.png"),
            height = 720,
            width = 1050,
            key = "Nerves"
        )

        

st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.title-font {
    font-size:50px !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.small-font {
    font-size:5px !important;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.image("E:\lvl alpha\CMS\imgs\ArmyLogo.png", caption=None,  use_column_width=True, clamp=True, channels="RGB", output_format="PNG")
forms = st.form("injuryform")

with forms :
      # Using object notation
     st.sidebar.subheader("Employee Name:","")
     st.sidebar.subheader("Employee ID:","")

     medic = st.sidebar.selectbox(
      "Select Name of Medic",
       ("Dr Sharma", "Dr Joshi "))
     add_selectbox1 = st.sidebar.selectbox(
    "Does Injury require Hospital / Physician?",
    ("Yes", "No "))

     type_injury = st.sidebar.selectbox(
    "Select type of injury",
    ("Skeleton    🦴", "Muscular   💪","Skin","Nervous      🧠"))





     st.markdown('<p class="title-font">Injury Details</p>', unsafe_allow_html=True)

     p1,p2 = st.columns(spec=2, gap="large")
     with p1:
         st.text("📅 injury:April 2, 2020; 13:00")
         st.text("Unit/Location: ")
    


     with p2:
      st.text("📅 first-aid:April 2, 2020; 13:20 ")
      st.text("Division: ")
     c1, c2, c3 = st.columns(3)
     c1.text_input("Injury Code")
     with c2:
        st.markdown('<p class="medium-font">Injury Score</p>', unsafe_allow_html=True)
        def injury_score():
          injury_score = 80
          progress_text = "Injury Score"
          my_bar = st.progress(injury_score)

          for percent_complete in range(injury_score, 10):
             my_bar.progress(percent_complete,progress_text,injury_score)
       
        injury_score()
     c3.markdown('<p class="medium-font">Burn Percentage%</p>', unsafe_allow_html=True)
     c3.selectbox("TBSA%",("Head 7%","Neck 2%","Anterior trunk 13%","Posterior trunk 13%","Right buttock 2.5%","Left buttock 2.5%","Genitalia 1%","R upper arm 4%","L upper arm 4%","R lower arm 3%","L lower arm 3%","R hand 2.5%","L hand 2.5%","R thigh 9.5%","Lthigh 9.5%","R leg 7%","L leg 7%","R foot 3.5%","Lfoot 3.5%"))
     c3.text_input("Fluid Requirements")
     
     st.markdown('<p class="big-font">INJURY</p>', unsafe_allow_html=True)
     st.selectbox("Injury",('A-ABRASION','AR-ARTILLERY',"B-BURN","BL-BLUNT","C-CONTUSION","D-DISCOLORATION","F-FRACTIRE",'FA-FALL',"GSW-GUN SHOT WOUND","GR-GRENADE","H-HAEMORRHAGE","L-LACERATION",'LM-LANDMINE',"P-PAIN","R-RIGIDITY","S-SWELLING","T-TENDERNESS","I-IED",'M-MVC','R-RPG'))
     st.markdown('<p class="big-font">Part of the Body</p>', unsafe_allow_html=True)
     c1,c2,c3 = st.columns(3)
     c1.checkbox("Front" )   
     c2.checkbox("Back")
     #c3 = st.selectbox("Severity of Injury",("MILD","MODERATE","SEVERE")
     c3.select_slider('Rate the severity of injury',
                           options=['Mild ','Moderate','Severe'])
                           #value=(1,5,10))


     if type_injury == "Skin":
         
    
   # with p1:
       st.markdown('<p class="big-font">Reported Visible Symptoms of injury</p>', unsafe_allow_html=True)
       c1, c2, c3,c4 = st.columns(4)
       c1.checkbox("Laceration",key= 1)
       c2.checkbox("Burn", key= 2)
       c3.checkbox("Rash", key= 3)
       c4.checkbox("Abrasion",key=33)
       t1= st.text_input("any others:", key= 4)
       st.file_uploader(label="Upload Pictures", type= ['png', 'jpg'], accept_multiple_files=True,key= 5,  label_visibility="visible")
       picture = st.camera_input("Take a picture")
       if picture:
        st.image(picture)
       st.write("---")
   # with p2:
       
       st.markdown('<p class="big-font">Treatment Provided</p>', unsafe_allow_html=True)
       c1, c2 = st.columns(2)
       c1.checkbox("Ointment",key= 6)
       c2.checkbox("Bandage",key= 7)
       t1= st.text_input("any others:", key= 8)
       c7, c8, c9 = st.columns(3)
       c7.selectbox("Medication", ("ADENOSINE","ASPIRIN","ATROPINE","DEXTROSE","MORPHINE","FENTANYL","HEPARIN","KETAMINE","LIDOCAINE","METOPROLOL","KETAMINE","OXYGEN","TETRACAINE","HEPARIN","CYANIDE ANTIDOTE KIT","IPRATROPIUM","TRANEXAMIC ACID (TXA)"))
       c8.selectbox("Route of Administration", ("Oral", "IV" , "IM"))
       c9.text_input("Drug Dosage")


       
       #st.button(label="Submit", type="primary", disabled=False, use_container_width=0)
         

#st.button(label="Add new injury", type="primary", disabled=False, use_container_width=0)



     if type_injury=="Skeleton    🦴":
      # with p1:
       
       st.markdown('<p class="big-font">Reported Visible Symptoms of injury</p>', unsafe_allow_html=True)
       c1, c2, c3 = st.columns(3)
       
       c1.checkbox("Inflammation",key= 9)
       c2.checkbox("Fracture", key= 10)
       c3.checkbox("Redness",key= 11)
       t2= st.text_input("any others:", key= 12)
       st.file_uploader(label="Upload Pictures", type= ['png', 'jpg'], accept_multiple_files=True,key= 13,  label_visibility="visible")
       picture = st.camera_input("Take a picture")
       if picture:
        st.image(picture)

       st.markdown('#') 

       st.markdown('<p class="big-font">Glasgow Coma Scale</p>', unsafe_allow_html=True)

       

       st.markdown('<p class="big-font">Best Motor Response</p>', unsafe_allow_html=True)

       c11, c12, c13 = st.columns(3)

       c11.checkbox("Obeys commands",key= 14)
       c11.checkbox("Localising",key= 15)
       c12.checkbox("Normal Flexion",key= 16)
       c12.checkbox("Abormal Flexion",key= 17)
       c13.checkbox("None",key= 18)
       c13.checkbox("Non testable",key= 19)


       st.markdown('#') 

       st.markdown('<p class="big-font">Verbal Response</p>', unsafe_allow_html=True)

       c21, c22, c23 = st.columns(3)

       c21.checkbox("Oriented",key= 20)
       c21.checkbox("Confused",key= 21)
       c22.checkbox("Words",key= 22)
       c22.checkbox("Sounds",key= 23)
       c23.checkbox("None",key= 24)
       c23.checkbox("Non testable",key= 25)

       st.markdown('#') 

       st.markdown('<p class="big-font">Verbal Response</p>', unsafe_allow_html=True)

       c31, c32 = st.columns(2)

       c31.checkbox("Spontaneous",key= 26)
       c31.checkbox("To sound",key= 27)
       c32.checkbox("None",key= 28)
       c32.checkbox("Non testable",key= 29)


       
       

       st.write("---")


       st.markdown('<p class="big-font">Treatment Provided</p>', unsafe_allow_html=True)
       c1, c2 = st.columns(2)
       c1.checkbox("Immobilization",key= 30)
       c2.checkbox("Plaster",key= 31)
       t1= st.text_input("any others:", key= 32)
       c7, c8, c9 = st.columns(3)
       c7.selectbox("Medication", ("ADENOSINE","ASPIRIN","ATROPINE","DEXTROSE","MORPHINE","FENTANYL","HEPARIN","KETAMINE","LIDOCAINE","METOPROLOL","KETAMINE","OXYGEN","TETRACAINE","HEPARIN","CYANIDE ANTIDOTE KIT","IPRATROPIUM","TRANEXAMIC ACID (TXA)"))
       c8.selectbox("Route of Administration", ("Oral", "IV" , "IM"))
       c9.text_input("Drug Dosage")

       
       #st.button(label="Add new injury", type="primary", disabled=False, use_container_width=0)
       #st.button(label="Submit", type="primary", disabled=False, use_container_width=0)
    
     if type_injury == "Muscular   💪":
    
   # with p1:
       st.markdown('<p class="big-font">Reported Visible Symptoms of injury</p>', unsafe_allow_html=True)
       c1, c2, c3,c4 = st.columns(4)
       c1.checkbox("Swelling",key= 34)
       c2.checkbox("Spasms", key= 35)
       c3.checkbox("Limited range of motion", key= 36)
       c4.checkbox("Cramping",key=37)
       t1= st.text_input("any others:", key= 38)
       st.file_uploader(label="Upload Pictures", type= ['png', 'jpg'], accept_multiple_files=True,key= 5,  label_visibility="visible")
       picture = st.camera_input("Take a picture")
       if picture:
        st.image(picture)
   # with p2:
       
       st.markdown('<p class="big-font">Treatment Provided</p>', unsafe_allow_html=True)
       c1, c2, c3,c4 = st.columns(4)
       c1.checkbox("Pain killer",key= 39)
       c2.checkbox("Cold compress/Heat",key= 40)
       c2.checkbox("RICE",key= 41)
       c2.checkbox("Physical exercise",key= 43)
       t1= st.text_input("Any others:", key= 44)
      

      
       c7, c8, c9 = st.columns(3)
       c7.selectbox("Medication", ("ADENOSINE","ASPIRIN","ATROPINE","DEXTROSE","MORPHINE","FENTANYL","HEPARIN","KETAMINE","LIDOCAINE","METOPROLOL","KETAMINE","OXYGEN","TETRACAINE","HEPARIN","CYANIDE ANTIDOTE KIT","IPRATROPIUM","TRANEXAMIC ACID (TXA)"))
       c8.selectbox("Route of Administration", ("Oral", "IV" , "IM"))
       c9.text_input("Drug Dosage")


     
                
     selectCanvas = st.radio("CALL",
                            options = ('REFINERY HOSPITAL', 'FIRST AID CENTRE', 'REFERRAL FOR MEDICAL ADVICE '),
                            horizontal = True,
                            label_visibility = 'hidden')

     st.form_submit_button("Submit")

st.button("Share ✉️")  


