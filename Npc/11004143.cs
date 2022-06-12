using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004143: Lian
/// </summary>
public class _11004143 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010557$
    // - Hahaha!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010558$
                // - $npcName:11001167[gender:0]$ likes to frighten us with scary stories, but now that I know better, I don't believe a word he says!
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
