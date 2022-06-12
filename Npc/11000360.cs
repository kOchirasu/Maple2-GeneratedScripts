using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000360: Yosef
/// </summary>
public class _11000360 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001496$
    // - What's wrong?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001498$
                // - Whew, it sure is hot here! I told my mom that I could make it on my own. Maybe I should've taken $npcName:11000420[gender:1]$'s advice and settled down in $map:02000111$ instead... 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
