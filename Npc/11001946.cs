using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001946: Cello Student
/// </summary>
public class _11001946 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1123165007007492$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1208184307007536$
                // - Finally, I'm in my element. Don't bother me while I'm in the zone.
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
