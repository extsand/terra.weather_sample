const burgAnimation = () =>{
	var burger = document.querySelector('.svgburg')
	 var path1 = document.querySelector('.path1')
	 var path2 = document.querySelector('.path2')
	 var mline = document.querySelector('.mline')
	 burger.addEventListener('click',() =>{     
			 path1.classList.toggle('cross');
			 path2.classList.toggle('cross');
			 mline.classList.toggle('hide');
			}
		)

}

burgAnimation()


const burgerMenu = document.querySelector('.burger-menu')
const nav = document.querySelector('.nav-main')


let toggle = false
burgerMenu.addEventListener('click', () => {
	if(!toggle){
		nav.classList.add('active')
		document.body.style.overflow = 'hidden'
		toggle = true
	}else{
		nav.classList.remove('active')
		document.body.style.overflow = 'visible'
		toggle = false
	}
})
