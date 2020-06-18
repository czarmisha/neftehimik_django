label = document.querySelector('.label');
        body = document.querySelector('body');

        label.addEventListener('click', function () {
            if (burger.checked) body.classList.remove('overflow');
            else body.classList.add('overflow');
        })