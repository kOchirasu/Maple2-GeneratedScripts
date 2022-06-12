using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000174: Broonie
/// </summary>
public class _11000174 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000728$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000730$
                // - Excuse me, but could you take $npcName:11000170[gender:0]$ with you? I've got things to do, and he keeps bothering me with some nonsense about love. I'm fine being friends, but that's it!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
