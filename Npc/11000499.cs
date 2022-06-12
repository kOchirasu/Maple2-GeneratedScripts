using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000499: Gogh
/// </summary>
public class _11000499 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002172$
    // - Did... Did you come to see me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002175$
                // - I thought that if we went deeper into the forest, we could keep $npcName:11000751[gender:1]$ safer...
                return 30;
            case (30, 1):
                // $script:0831180407002176$
                // - Others pointed their fingers and called us cowards, but we didn't care. We just wanted to keep our charge safe... 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
