using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001192: Pirollo
/// </summary>
public class _11001192 : NpcScript {
    internal _11001192(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1016202007004172$ 
                // - Grah! Writer's block, my mortal enemy!
                return true;
            case 30:
                // $script:1016202007004175$ 
                // - <font color="#909090"> (He sighs.)</font>
                //   Am I really qualified to be a TV writer...? Hey, you there! Can I ask you a question?
                // $script:1016210507004209$ 
                // - Do you think people should pursue jobs they <i>want</i> to do, or just ones they're good at?
                switch (selection) {
                    // $script:1016210507004210$
                    // - I'm not sure... What do you think?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:1016210507004211$
                    // - Why? Do you not like your job?
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:1016202007004178$ 
                // - What I want to do, of course! I would give anything to be good at what I <i>want</i> to be doing...
                return true;
            case 32:
                // $script:1016202007004179$ 
                // - That's not it. This has been my dream job for as long as I can remember. It's just... not the job I expected.
                //   <font color="#909090">(He sighs.)</font>
                return true;
            default:
                return true;
        }
    }
}
