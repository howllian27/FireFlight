export default function Vector3(props: Vector3Props) {
  return (
    <div className={`${props.className}`}>
      <svg
        width="100%"
        height="100%"
        preserveAspectRatio="none"
        viewBox="0 0 25 26"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M 24.658 21.616 L 19.79 16.748 C 19.57 16.528 19.273 16.406 18.96 16.406 H 18.164 C 19.512 14.683 20.313 12.515 20.313 10.156 C 20.313 4.546 15.767 0 10.156 0 C 4.546 0 0 4.546 0 10.156 C 0 15.767 4.546 20.313 10.156 20.313 C 12.515 20.313 14.683 19.512 16.406 18.164 V 18.96 C 16.406 19.273 16.528 19.57 16.748 19.79 L 21.616 24.658 C 22.075 25.117 22.817 25.117 23.272 24.658 L 24.653 23.276 C 25.112 22.817 25.112 22.075 24.658 21.616 Z M 10.156 16.406 C 6.704 16.406 3.906 13.613 3.906 10.156 C 3.906 6.704 6.699 3.906 10.156 3.906 C 13.608 3.906 16.406 6.699 16.406 10.156 C 16.406 13.608 13.613 16.406 10.156 16.406 Z"
          fill="#BAB9B9"
         />
      </svg>
    </div>
  );
}

Vector3.defaultProps = {
  className: "",
};

interface Vector3Props {
  className: string;
}

/**
 * This component was generated from Figma with FireJet.
 * Learn more at https://www.firejet.io
 *
 * README:
 * The output code may look slightly different when copied to your codebase. To fix this:
 * 1. Include the necessary fonts. The required fonts are imported from public/index.html
 * 2. Include the global styles. They can be found in App.css
 *
 * Note: Step 2 is not required for tailwind.css output
 */
