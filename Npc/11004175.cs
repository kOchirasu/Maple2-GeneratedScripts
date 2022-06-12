using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004175: Girl
/// </summary>
public class _11004175 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010612$
    // - Today is the best day of my life!!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010613$
                // - Eek! It's $npcName:11004174[gender:0]$! It's really $npcName:11004174[gender:0]$!! I can't believe it, I think I'm gonna die.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
