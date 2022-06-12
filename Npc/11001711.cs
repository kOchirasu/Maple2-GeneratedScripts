using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001711: Tinchai
/// </summary>
public class _11001711 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0728022507006963$
    // - Mm? What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0728024507006995$
                // - The more I look at this place, the more mystified I am. Almost as if... it yearns for something...
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
