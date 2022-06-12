using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004182: Ishura
/// </summary>
public class _11004182 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010626$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010627$
                // - Simply hiding is no strategy for victory. Especially up against the likes of an expert tracker like Arazaad.
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
