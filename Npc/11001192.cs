using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001192: Pirollo
/// </summary>
public class _11001192 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1016202007004172$
    // - Grah! Writer's block, my mortal enemy!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1016202007004175$
                // - <font color="#909090"> (He sighs.)</font>
                //   Am I really qualified to be a TV writer...? Hey, you there! Can I ask you a question?
                return 30;
            case (30, 1):
                // $script:1016210507004209$
                // - Do you think people should pursue jobs they <i>want</i> to do, or just ones they're good at?
                switch (selection) {
                    // $script:1016210507004210$
                    // - I'm not sure... What do you think?
                    case 0:
                        return 31;
                    // $script:1016210507004211$
                    // - Why? Do you not like your job?
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:1016202007004178$
                // - What I want to do, of course! I would give anything to be good at what I <i>want</i> to be doing...
                return -1;
            case (32, 0):
                // $script:1016202007004179$
                // - That's not it. This has been my dream job for as long as I can remember. It's just... not the job I expected.
                //   <font color="#909090">(He sighs.)</font>
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
