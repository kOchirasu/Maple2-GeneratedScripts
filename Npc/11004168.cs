using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004168: Joddy
/// </summary>
public class _11004168 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010591$
    // - Ah... What should I do?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010592$
                // - Ohh gee, oh man... I don't know about this royale thing.
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
