document.addEventListener('DOMContentLoaded', function() {
    let modal = document.querySelectorAll('.modal');
    M.Modal.init(modal, {});
    let modalInstance = M.Modal.getInstance(modal[0])

    let slider = document.querySelector(".slider")
    let sliderInstance = M.Slider.init(slider, {
        height: 200,
        indicators: false,
        interval: 1000
    })

    let carousel = document.querySelector(".carousel")
    let carouselInstance = M.Carousel.init(carousel, {
        fullWidth: true
    })

    const input_lagu = document.querySelector("#input_file")
    const input_nama_lagu = document.querySelector("#input_file_name")
    const file_box_input = document.querySelector("#file-box-input")
    const preloader = document.querySelector("#preloader")
    file_box_input.className = "col s12"
    preloader.style.display = "none"

    document.querySelector("#lagu_submit").addEventListener('click', () => {
        console.log(input_lagu.value)
        if(input_lagu.files[0]){
            file_box_input.className = "col s10"
            preloader.removeAttribute("style")
            const formData = new FormData()
            formData.append("lagu",input_lagu.files[0])

            fetch('/predict', {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(res => {
                if(res.result == "success"){
                    const list_collection = document.querySelector("#list-collection")
                    file_box_input.className = "col s12"
                    preloader.style.display = "none"
    
                    for(let segment in res.data){
    
                        let tags = []
                        for(const key in res.data[segment]){
                            tags.push(key)
                        }
    
                        const li = document.createElement('li')
                        const img = document.createElement('img')
                        const span = document.createElement('span')
                        const strong = document.createElement('strong')
                        const p = document.createElement('p')
    
                        img.src = "/static/img/musical-note.png"
                        img.className = "circle responsive-img"
                        strong.innerText = segment
                        span.append(strong)
                        p.append(`Tags : ${tags.join()}`)
    
                        li.className = "collection-item avatar"
                        li.append(img, span, p)
                        list_collection.append(li)
                    }
    
                    const title_lagu = document.querySelector("#title-lagu")
                    title_lagu.innerText = input_lagu.files[0].name
                    modalInstance.close()
                    input_lagu.value = ""
                    input_nama_lagu.value = ""
                }
                else{
                    alert("ekstensi file tidak sesuai")
                }
            })
        }
        else{
            alert("input tidak boleh kosong")
        }
    })

});

