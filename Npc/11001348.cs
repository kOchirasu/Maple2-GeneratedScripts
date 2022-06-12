using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001348: Cathy Catalina
/// </summary>
public class _11001348 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217012607005305$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217012607005308$
                // -  I came here to expand my business, but my partner is being completely impossible. And on top of that, the weather's too hot here and the people are too stubborn. What a terrible day...
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
