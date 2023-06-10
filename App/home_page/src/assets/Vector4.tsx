export default function Vector4(props: Vector4Props) {
  return (
    <div className={`${props.className}`}>
      <svg
        width="100%"
        height="100%"
        preserveAspectRatio="none"
        viewBox="0 0 14 22"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M 0.477 9.832 L 9.689 0.485 C 10.325 -0.162 11.355 -0.162 11.985 0.485 L 13.516 2.038 C 14.152 2.684 14.152 3.729 13.516 4.368 L 6.993 11 L 13.523 17.625 C 14.159 18.272 14.159 19.316 13.523 19.955 L 11.992 21.516 C 11.355 22.162 10.325 22.162 9.695 21.516 L 0.483 12.168 C-0.16 11.522 -0.16 10.478 0.477 9.832 V 9.832 Z"
          fill="black"
         />
      </svg>
    </div>
  );
}

Vector4.defaultProps = {
  className: "",
};

interface Vector4Props {
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
