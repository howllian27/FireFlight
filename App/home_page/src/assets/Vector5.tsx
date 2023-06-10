export default function Vector5(props: Vector5Props) {
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
          d="M 13.523 12.168 L 4.307 21.516 C 3.67 22.162 2.64 22.162 2.009 21.516 L 0.478 19.962 C-0.159 19.316 -0.159 18.272 0.478 17.632 L 7.011 11.007 L 0.478 4.381 C-0.159 3.735 -0.159 2.691 0.478 2.052 L 2.003 0.485 C 2.64 -0.162 3.67 -0.162 4.3 0.485 L 13.516 9.832 C 14.16 10.478 14.16 11.522 13.523 12.168 V 12.168 Z"
          fill="#FC5710"
         />
      </svg>
    </div>
  );
}

Vector5.defaultProps = {
  className: "",
};

interface Vector5Props {
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
