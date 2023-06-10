export default function Vector8(props: Vector8Props) {
  return (
    <div className={`${props.className}`}>
      <svg
        width="100%"
        height="100%"
        preserveAspectRatio="none"
        viewBox="0 0 20 27"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M 8.972 26.455 C 1.405 15.347 0 14.207 0 10.125 C 0 4.533 4.477 0 10 0 C 15.523 0 20 4.533 20 10.125 C 20 14.207 18.595 15.347 11.028 26.455 C 10.531 27.182 9.469 27.182 8.972 26.455 Z M 10 14.344 C 12.301 14.344 14.167 12.455 14.167 10.125 C 14.167 7.795 12.301 5.906 10 5.906 C 7.699 5.906 5.833 7.795 5.833 10.125 C 5.833 12.455 7.699 14.344 10 14.344 Z"
          fill="#FC5710"
         />
      </svg>
    </div>
  );
}

Vector8.defaultProps = {
  className: "",
};

interface Vector8Props {
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
