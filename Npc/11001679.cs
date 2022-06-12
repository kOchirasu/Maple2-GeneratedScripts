using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001679: Bravos
/// </summary>
public class _11001679 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0629000607006447$
    // - You need anything, you just call out my name. Not that I'll come running, but maybe it'll give you good luck.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0629000607006450$
                // - Do you know why I'm called $npcName:11001545[gender:0]$?
                switch (selection) {
                    // $script:0629000607006451$
                    // - You want to ask me that? Right now?
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:0629000607006453$
                // - You're no fun. Forget it.
                switch (selection) {
                    // $script:0706165507006639$
                    // - How are you feeling?
                    case 0:
                        return 50;
                }
                return -1;
            case (50, 0):
                // $script:0629000607006454$
                // - Wh-what? You worried about me? Don't! Look... You're giving me goosebumps!
                return 50;
            case (50, 1):
                // $script:0629000607006456$
                // - What's with the intense stare? Spit it out or sc-scram!
                //   <font color="#909090">(He's blushing.)</font>
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.Next,
            (50, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
