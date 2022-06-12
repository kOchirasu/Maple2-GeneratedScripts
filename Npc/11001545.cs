using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001545: Bravos
/// </summary>
public class _11001545 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0516130207006113$
    // - Ugh. Now what?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0531170907006223$
                // - Hey! You know why they call me $npc:11001545[gender:0]$?
                switch (selection) {
                    // $script:0531170907006224$
                    // - No clue.
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:0531170907006225$
                // - 'Cause I'm so great I deserve a standing ovation! Haha! I can't believe you never heard of me. Anyway, you need anything, you just call out my name. Not that I'll come running, but maybe it'll give you good luck.
                return 20;
            case (20, 1):
                // $script:0607145407006336$
                // - Well what're you staring at? Did'ja have something to tell me, or do you just like the view?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
