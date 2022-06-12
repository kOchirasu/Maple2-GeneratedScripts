using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000504: Rue
/// </summary>
public class _11000504 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002187$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217012607005230$
                // - This place is... How do I say? Full of contradictions. A rich, gorgeous facade that hides a lingering melancholy. This hotel is luxurious, but it's not for the regular people who live around it. Those people belong to a different world.
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
