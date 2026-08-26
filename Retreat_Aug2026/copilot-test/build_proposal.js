// Synthetic ECON3500 RP-04 research proposal — deliberately "medium quality" (~29/38).
// Planted flaws are documented in ANSWER_KEY.md. Author is fictional.
const fs = require("fs");
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, HeadingLevel,
        AlignmentType, BorderStyle, WidthType, ShadingType, Footer, PageNumber } = require("docx");

const P = (text, opts = {}) => new Paragraph({
  spacing: { after: 160, line: 300 },
  alignment: AlignmentType.LEFT,
  children: Array.isArray(text) ? text : [new TextRun({ text, ...opts })],
});
const H1 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun(t)] });
const I = (t) => new TextRun({ text: t, italics: true });
const T = (t) => new TextRun(t);

// ---------- Summary statistics table ----------
const border = { style: BorderStyle.SINGLE, size: 4, color: "000000" };
const none = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const W = [4200, 1720, 1720, 1720];
const cell = (text, { bold = false, align = AlignmentType.LEFT, top = none, bottom = none, fill } = {}, w) =>
  new TableCell({
    width: { size: w, type: WidthType.DXA },
    borders: { top, bottom, left: none, right: none },
    shading: fill ? { fill, type: ShadingType.CLEAR } : undefined,
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    children: [new Paragraph({ alignment: align, keepNext: true, children: [new TextRun({ text, bold, size: 20 })] })],
  });
const row = (cells, opts = {}) => new TableRow({
  cantSplit: true,
  children: cells.map((c, i) => cell(c, { align: i === 0 ? AlignmentType.LEFT : AlignmentType.CENTER, ...opts }, W[i])),
});
const stats = [
  ["In labor force (=1)", "0.68", "0.47", "112,430"],
  ["PFL in effect in state (=1)", "0.31", "0.46", "112,430"],
  ["Age", "33.2", "6.1", "112,430"],
  ["Bachelor's degree or higher (=1)", "0.41", "0.49", "112,430"],
  ["Married (=1)", "0.74", "0.44", "112,430"],
  ["nchild", "1.9", "0.9", "112,430"],
  ["Hispanic (=1)", "0.24", "0.43", "112,430"],
  ["Youngest child under 1 (=1)", "0.22", "0.41", "112,430"],
];
const table = new Table({
  width: { size: 9360, type: WidthType.DXA },
  columnWidths: W,
  rows: [
    row(["Variable", "Mean", "Std. dev.", "N"], { bold: true, top: border, bottom: border }),
    ...stats.map((r) => row(r)),
    row(["Number of states", "51", "", ""], { top: border }),
    row(["Number of survey years", "14", "", ""], { bottom: border }),
  ],
});

// ---------- Document ----------
const doc = new Document({
  styles: {
    default: { document: { run: { font: "Times New Roman", size: 24 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: "Times New Roman" },
        paragraph: { spacing: { before: 280, after: 120 }, outlineLevel: 0 } },
    ],
  },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER,
      children: [new TextRun({ children: [PageNumber.CURRENT], size: 20 })] })] }) },
    children: [
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 },
        children: [new TextRun({ text: "Paid Family Leave and Mothers' Labor Force Participation: Evidence from State Policies, 2010–2023", bold: true, size: 28 })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: [new TextRun("Andy Dwyer")] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 360 }, children: [new TextRun("ECON 3500 — Research Proposal — April 9, 2026")] }),

      H1("1. Introduction"),
      P("How does paid family leave affect mothers? Since California introduced the first state paid family leave (PFL) program in 2004, eight states have adopted programs that replace part of a worker's wages for several weeks after the birth of a child. Supporters argue that paid leave keeps mothers attached to their jobs, while critics worry that it raises costs for employers and could reduce hiring of women of childbearing age. In this paper I ask whether state PFL laws increase the labor force participation of mothers with young children."),
      P([T("This question matters because women's labor force participation in the United States has stalled since the 1990s and has fallen behind most other rich countries. Blau and Kahn (2013) find that almost a third of the gap between the U.S. and other OECD countries can be explained by the absence of family-friendly policies such as paid leave. Goldin (2014) argues that the \"last chapter\" of gender convergence depends on the flexibility of jobs, and paid leave is one of the main policies that can change how costly it is for a mother to stay employed. The "), I("family gap"), T(" in pay documented by Waldfogel (1998) also suggests that the years right after a birth are when women's careers are most vulnerable.")]),
      P("To answer this question I use the Current Population Survey Annual Social and Economic Supplement (CPS ASEC) from 2010 to 2023, obtained through IPUMS. I compare mothers of children under five in states with a PFL program in effect to mothers in states without one, controlling for individual characteristics and for state and year fixed effects. This paper will show the causal effect of paid leave on mothers' employment and help policymakers in states that are currently debating PFL legislation."),

      H1("2. Literature Review"),
      P("The most studied PFL program is California's. Rossin-Slater, Ruhm, and Waldfogel (2013) use the CPS and a difference-in-differences design to show that California's program roughly doubled leave-taking among mothers of infants and increased weekly hours and wages of mothers of one- to three-year-olds. The effects were largest for less-advantaged mothers, who previously had little access to paid leave."),
      P("Baum and Ruhm (2016) use the National Longitudinal Survey of Youth 1997 and find that California's PFL raised the probability that mothers were working one year after birth by about 18 percent, and also increased hours and weekly earnings. They interpret these results as evidence that paid leave strengthens job continuity."),
      P("Byker (2016) looks at both California and New Jersey and uses monthly CPS data to study labor force attachment around childbirth. She finds that short-duration paid leave increases labor force participation in the months around a birth, mainly for women without a college degree, because the leave allows them to remain employed instead of quitting."),
      P("Bailey, Byker, Patel, and Ramnath (2019) take a longer view using tax data and find that, ten years later, mothers who were eligible for California's PFL had slightly lower employment and earnings than those who were not. This is surprising and suggests that the short-run and long-run effects can go in different directions."),
      P("These five peer-reviewed studies all focus on one or two early-adopting states. My paper fits in by using data from all states through 2023, which includes the newer programs in New York, Washington, Massachusetts, Connecticut, and Oregon, so the results are not only about California."),

      H1("3. Data"),
      P("I use the CPS ASEC for the years 2010 through 2023, downloaded from IPUMS CPS (Flood et al., 2023). The ASEC is a nationally representative survey of about 200,000 people each March and records labor force status, demographic characteristics, and state of residence. My sample is women aged 20 to 45 whose youngest own child in the household is under five years old. I dropped observations with missing values on education or marital status. The final sample has 112,430 mothers across 51 states (including Washington, D.C.) and 14 survey years."),
      P("The dependent variable is an indicator equal to one if the mother is in the labor force (employed or looking for work) during the survey reference week. The key independent variable is an indicator equal to one if a state PFL program was paying benefits in that state in that year. I coded PFL from the effective dates of each program: California (2004), New Jersey (2009), Rhode Island (2014), New York (2018), Washington (2020), Massachusetts (2021), Connecticut (2022), and Oregon (2023). Control variables are age, an indicator for a bachelor's degree or higher, marital status, number of own children, and Hispanic ethnicity."),
      new Paragraph({ keepNext: true, spacing: { after: 160, line: 300 }, children: [new TextRun("Table 1 reports summary statistics. About 68 percent of mothers in the sample are in the labor force, and 31 percent of observations are in a state-year with PFL in effect. The average mother is 33 years old and has about two children.")] }),
      // (replaced) P("Table 1 reports summary statistics. About 68 percent of mothers in the sample are in the labor force, and 31 percent of observations are in a state-year with PFL in effect. The average mother is 33 years old and has about two children."),
      new Paragraph({ keepNext: true, spacing: { before: 120, after: 80 }, children: [new TextRun({ text: "Table 1. Summary statistics, mothers of children under five, CPS ASEC 2010–2023", bold: true })] }),
      table,
      new Paragraph({ spacing: { before: 60, after: 200 }, children: [new TextRun({ text: "Source: IPUMS CPS ASEC 2010–2023. Sample is women aged 20–45 with youngest own child under five. Unweighted.", size: 20, italics: true })] }),

      H1("4. Empirical Specification"),
      P("I estimate the following linear probability model by OLS:"),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 120, after: 120 },
        children: [new TextRun({ text: "LFP", italics: true }), new TextRun({ text: "ist", subScript: true, italics: true }),
          new TextRun(" = β"), new TextRun({ text: "0", subScript: true }),
          new TextRun(" + β"), new TextRun({ text: "1", subScript: true }), new TextRun({ text: " PFL", italics: true }), new TextRun({ text: "st", subScript: true, italics: true }),
          new TextRun(" + "), new TextRun({ text: "X", italics: true }), new TextRun({ text: "ist", subScript: true, italics: true }), new TextRun("′γ + α"), new TextRun({ text: "s", subScript: true }),
          new TextRun(" + δ"), new TextRun({ text: "t", subScript: true }), new TextRun(" + ε"), new TextRun({ text: "ist", subScript: true })] }),
      P([T("where "), I("LFP"), T(" is an indicator equal to one if mother "), I("i"), T(" in state "), I("s"), T(" in year "), I("t"), T(" is in the labor force, "), I("PFL"), T(" is an indicator equal to one if a paid family leave program is in effect in state "), I("s"), T(" in year "), I("t"), T(", "), I("X"), T(" is a vector of individual controls, α"), new TextRun({ text: "s", subScript: true }), T(" are state fixed effects, δ"), new TextRun({ text: "t", subScript: true }), T(" are year fixed effects, and ε is the error term. The coefficient of interest is β"), new TextRun({ text: "1", subScript: true }), T(", which captures the effect of PFL on the probability that a mother is in the labor force, holding constant her characteristics and fixed differences across states and years.")]),
      P("The state fixed effects absorb permanent differences between states, such as California always having higher female labor force participation than Alabama. The year fixed effects absorb national shocks such as the 2020 pandemic, which is important because several states adopted PFL around that time."),

      H1("5. Planned Analysis"),
      P("I will first estimate the model with only the PFL indicator and fixed effects, and then add the individual controls to see whether the estimate changes. I expect β1 to be positive and in the range of 2 to 4 percentage points based on the California estimates in the literature. I will then estimate the model separately for mothers whose youngest child is under one year old, since these are the mothers most likely to be on leave or deciding whether to return to work, and for mothers with and without a bachelor's degree, since Byker (2016) finds larger effects for less-educated women. If β1 is positive and statistically significant, this will prove that paid leave increases mothers employment."),

      H1("6. Threats and Limitations"),
      P("The main threat to interpreting β1 as the effect of PFL is omitted variable bias. States that adopt PFL are richer, more liberal, and have stronger labor markets for women than states that do not, and all of these are correlated with higher female labor force participation. This would bias β1 upward. The state fixed effects address the part of this that is constant over time, and the year fixed effects address national trends, but if PFL states were already on a different trend before adopting the policy, the bias would remain. Reverse causality is unlikely, because an individual mother's labor force decision does not effect whether her state passes a law."),
      P("Measurement error is a second concern. The CPS does not record whether a mother is actually on paid leave, and a mother on leave is counted as employed, so my dependent variable measures attachment to the labor force rather than actual work. It's also possible that some mothers moved to a PFL state because of the policy, which would make the PFL indicator partly a choice rather than something that happened to them, however I expect this to be small."),

      H1("References"),
      ...[
        "Bailey, M. J., Byker, T. S., Patel, E., & Ramnath, S. (2019). The long-term effects of California's 2004 paid family leave act on women's careers: Evidence from U.S. tax data. NBER Working Paper No. 26416.",
        "Baum, C. L., & Ruhm, C. J. (2016). The effects of paid family leave in California on labor market outcomes. Journal of Policy Analysis and Management, 35(2), 333–356.",
        "Blau, F. D., & Kahn, L. M. (2013). Female labor supply: Why is the United States falling behind? American Economic Review, 103(3), 251–256.",
        "Byker, T. S. (2016). Paid parental leave laws in the United States: Does short-duration leave affect women's labor-force attachment? American Economic Review, 106(5), 242–246.",
        "Flood, S., King, M., Rodgers, R., Ruggles, S., Warren, J. R., Backman, D., Chen, A., Cooper, G., Richards, S., Schouweiler, M., & Westberry, M. (2023). IPUMS CPS: Version 11.0 [dataset]. Minneapolis, MN: IPUMS.",
        "Goldin, C. (2014). A grand gender convergence: Its last chapter. American Economic Review, 104(4), 1091–1119.",
        "Rossin-Slater, M., Ruhm, C. J., & Waldfogel, J. (2013). The effects of California's paid family leave program on mothers' leave-taking and subsequent labor market outcomes. Journal of Policy Analysis and Management, 32(2), 224–245.",
      ].map((r) => new Paragraph({ spacing: { after: 120 }, indent: { left: 720, hanging: 720 }, children: [new TextRun(r)] })),
    ],
  }],
});

Packer.toBuffer(doc).then((buf) => { fs.writeFileSync("proposal_medium_PFL.docx", buf); console.log("wrote proposal_medium_PFL.docx"); });
