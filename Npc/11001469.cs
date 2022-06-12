using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001469: Arl
/// </summary>
public class _11001469 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1223040807005536$
    // - This must be the place.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1223040807005539$
                // - Shhh! Don't tell my mom I'm here!
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
