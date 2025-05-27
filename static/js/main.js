      // Navbar scroll effect
      window.addEventListener("scroll", function () {
        const navbar = document.querySelector(".modern-navbar");
        if (window.scrollY > 50) {
          navbar.classList.add("scrolled");
        } else {
          navbar.classList.remove("scrolled");
        }
      });
      
      // Update cart total (demo)
      function updateCartTotal(count) {
        document.getElementById("cart-total").textContent = count;
      }
