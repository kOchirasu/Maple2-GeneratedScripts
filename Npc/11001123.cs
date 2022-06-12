using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001123: Gerome
/// </summary>
public class _11001123 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0910171307003837$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0915135007003943$
                // - The scientists in $map:2000270$ are known for their constant innovation. They're the reason I lug these heavy, expensive components everywhere I go.
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
