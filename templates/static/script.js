const testimonials = document.querySelectorAll(".testimonial");
const prevBtn = document.querySelector(".prev");
const nextBtn = document.querySelector(".next");

let activeTestimonial = 0;

function showTestimonial() {
  testimonials.forEach((testimonial) => {
    testimonial.classList.remove("active");
  });

  testimonials[activeTestimonial].classList.add("active");
}

prevBtn.addEventListener("click", () => {
activeTestimonial--;
if (activeTestimonial < 0) {
activeTestimonial = testimonials.length - 1;
}
showTestimonial();
});

nextBtn.addEventListener("click", () => {
activeTestimonial++;
if (activeTestimonial >= testimonials.length) {
activeTestimonial = 0;
}
showTestimonial();
});

showTestimonial();