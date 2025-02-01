
  const toggleBtn = document.querySelector('.toggle-btn');
const priceRangeOptions = document.querySelector('.price-range-options');
const investInput = document.querySelector('.invest-input');

// Add click event listener to the toggle button
toggleBtn.addEventListener('click', function () {
    const isVisible = priceRangeOptions.style.display === 'block';

    // Toggle dropdown visibility
    priceRangeOptions.style.display = isVisible ? 'none' : 'block';

    // Change the arrow direction
    toggleBtn.innerHTML = isVisible ? '&gt;' : '&lt;'; // Down (>) or up (<)
});

// Add event listeners to all radio buttons
document.querySelectorAll('.price-range-options input[type="radio"]').forEach((radio) => {
    radio.addEventListener('change', function () {
        // Update the input field value with the selected price range
        investInput.value = this.value;

        // Hide the dropdown
        priceRangeOptions.style.display = 'none';

        // Reset the arrow direction to down
        toggleBtn.innerHTML = '&gt;';
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const track = document.querySelector('.carousel-track');
    const dots = document.querySelectorAll('.dot');
    const prevBtn = document.querySelector('.prev');
    const nextBtn = document.querySelector('.next');
    let currentIndex = 0;

    const updateCarousel = (index) => {
        const width = track.querySelector('img').clientWidth;
        track.style.transform = `translateX(-${index * width}px)`;
        dots.forEach(dot => dot.classList.remove('active'));
        dots[index].classList.add('active');
    };

    nextBtn.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % dots.length;
        updateCarousel(currentIndex);
    });

    prevBtn.addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + dots.length) % dots.length;
        updateCarousel(currentIndex);
    });

    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            currentIndex = index;
            updateCarousel(currentIndex);
        });
    });
});


document.addEventListener('DOMContentLoaded', function () {
  // Select all <li> elements
  const listItems = document.querySelectorAll('li');

  // Add event listeners to each <li>
  listItems.forEach((item) => {
    item.addEventListener('click', function () {
      // Check if a message already exists below the clicked <li>
      const existingMessage = item.querySelector('.message');

      // If a message already exists, remove it
      if (existingMessage) {
        existingMessage.remove();
      } else {
        // Create a new <div> element to display the message
        const message = document.createElement('div');
        message.classList.add('message');
        let messageText = '';

        // Extract only the text content of the <li>
        const itemText = item.firstChild.textContent.trim(); // FirstChild is the text node

        // Set the message based on the clicked <li>
        switch (itemText) {
          case 'Case Review':
            messageText =
              'Performing preliminary checks to assess whether your case can result in a substantial recovery. Based on our experience.';
            break;
          case 'Evidence Gathering':
            messageText =
              'Gathering evidence to support your case with thorough research.';
            break;
          case 'Investigation Report':
            messageText =
              'Creating a detailed report of the investigation findings for you.';
            break;
          case 'Recommended Action Plan':
            messageText =
              'Providing actionable steps based on the findings of the investigation.';
            break;
          case 'Consultation Call':
            messageText =
              'Scheduling a free consultation call to discuss the case.';
            break;
          case 'Preliminary Case Review':
            messageText =
              'Performing a quick review of the case to assess the potential for further investigation.';
            break;
          case 'Asset Movement Investigation':
            messageText =
              'Investigating the movement of assets related to the case.';
            break;
          case 'Perpetrators Investigation':
            messageText =
              'Investigating the individuals responsible for the fraudulent activities.';
            break;
          default:
            messageText = 'No details available.';
        }

        // Set the text of the new message
        message.textContent = messageText;

        // Append the message below the clicked <li>
        item.appendChild(message);
      }
    });
  });
});



  const track = document.querySelector('.carousel-track');
  const slides = Array.from(track.children);
  const prevButton = document.querySelector('.prev-btn');
  const nextButton = document.querySelector('.next-btn');
  const dotsNav = document.querySelector('.carousel-nav');
  const dots = Array.from(dotsNav.children);
  
  const slideWidth = slides[0].getBoundingClientRect().width;
  let currentIndex = 0;
  
  // Function to move to the target slide
  function moveToSlide(track, targetIndex) {
    track.style.transform = `translateX(-${slideWidth * targetIndex}px)`;
  }
  
  // Function to update dot states
  function updateDots(currentDot, targetDot) {
    currentDot.classList.remove('active');
    targetDot.classList.add('active');
  }
  
  // Function to hide/show arrows
  function toggleArrows(currentIndex, slides, prevButton, nextButton) {
    prevButton.style.visibility = currentIndex === 0 ? 'hidden' : 'visible';
    nextButton.style.visibility = currentIndex === slides.length - 1 ? 'hidden' : 'visible';
  }
  
  // Initial arrow state
  toggleArrows(currentIndex, slides, prevButton, nextButton);
  
  // Event listener for previous button
  prevButton.addEventListener('click', () => {
    const currentDot = dotsNav.querySelector('.active');
    const prevIndex = currentIndex - 1;
  
    if (prevIndex >= 0) {
      moveToSlide(track, prevIndex);
      updateDots(currentDot, dots[prevIndex]);
      currentIndex = prevIndex;
      toggleArrows(currentIndex, slides, prevButton, nextButton);
    }
  });
  
  // Event listener for next button
  nextButton.addEventListener('click', () => {
    const currentDot = dotsNav.querySelector('.active');
    const nextIndex = currentIndex + 1;
  
    if (nextIndex < slides.length) {
      moveToSlide(track, nextIndex);
      updateDots(currentDot, dots[nextIndex]);
      currentIndex = nextIndex;
      toggleArrows(currentIndex, slides, prevButton, nextButton);
    }
  });
  
  // Event listener for dots navigation
  dotsNav.addEventListener('click', (e) => {
    const targetDot = e.target.closest('button');
    if (!targetDot) return;
  
    const currentDot = dotsNav.querySelector('.active');
    const targetIndex = dots.indexOf(targetDot);
  
    moveToSlide(track, targetIndex);
    updateDots(currentDot, targetDot);
    currentIndex = targetIndex;
    toggleArrows(currentIndex, slides, prevButton, nextButton);
  });



  const accordions = document.querySelectorAll('.accordion-header');
  accordions.forEach(header => {
      header.addEventListener('click', () => {
          const content = header.nextElementSibling;
          content.style.display = content.style.display === 'block' ? 'none' : 'block';
      });
  });

  document.addEventListener('DOMContentLoaded', () => {
    const dots = document.querySelectorAll('.dot');
    const items = document.querySelectorAll('.carousel-item');
    let currentIndex = 0;
  
    function updateCarousel() {
      items.forEach((item, index) => {
        item.style.display = index === currentIndex ? 'block' : 'none';
      });
  
      dots.forEach((dot, index) => {
        dot.classList.toggle('active', index === currentIndex);
      });
    }
  
    document.querySelector('.prev-slide').addEventListener('click', () => {
      currentIndex = (currentIndex - 1 + items.length) % items.length;
      updateCarousel();
    });
  
    document.querySelector('.next-slide').addEventListener('click', () => {
      currentIndex = (currentIndex + 1) % items.length;
      updateCarousel();
    });
  
    dots.forEach((dot, index) => {
      dot.addEventListener('click', () => {
        currentIndex = index;
        updateCarousel();
      });
    });
  
    updateCarousel(); // Initialize the carousel
  });
  

  function hideCookieBanner() {
    const banner = document.getElementById("cookie-banner");
    banner.style.display = "none"; // Hide the banner
  }
  

  document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.querySelector(".toggle-btn");
    const priceRangeOptions = document.querySelector(".price-range-options");
    const investInput = document.querySelector(".invest-input");

    toggleBtn.addEventListener("click", function () {
        const isVisible = priceRangeOptions.style.display === "block";
        priceRangeOptions.style.display = isVisible ? "none" : "block";
    });

    priceRangeOptions.addEventListener("change", function (event) {
        if (event.target.name === "investment") {
            investInput.value = event.target.value;
            priceRangeOptions.style.display = "none";
        }
    });
});


const countryDropdown = document.getElementById('country-dropdown');
const countryCodeBtn = document.getElementById('country-code-btn');
const selectedCode = document.getElementById('selected-code');
const selectedFlag = document.getElementById('selected-flag');
const dropdownArrow = document.getElementById('dropdown-arrow');

countryCodeBtn.addEventListener('click', (event) => {
  event.stopPropagation();
  const isOpen = countryDropdown.style.display === 'block';
  countryDropdown.style.display = isOpen ? 'none' : 'block';
  dropdownArrow.textContent = isOpen ? '▼' : '▲';  // Toggle arrow direction
});

countryDropdown.addEventListener('click', (event) => {
  const listItem = event.target.closest('li');
  if (listItem) {
    const code = listItem.getAttribute('data-code');
    const flag = listItem.getAttribute('data-flag');
    selectedCode.textContent = code;
    selectedFlag.src = flag;
    countryDropdown.style.display = 'none';
    dropdownArrow.textContent = '▼'; // Reset the arrow direction after selection
  }
});

// Close dropdown if clicking outside
document.addEventListener('click', () => {
  countryDropdown.style.display = 'none';
  dropdownArrow.textContent = '▼'; // Reset the arrow when closing
});