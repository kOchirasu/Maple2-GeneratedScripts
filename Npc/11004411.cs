using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004411: Nairin
/// </summary>
public class _11004411 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1113161307011839$
    // - Would you like to take on a mission for Green Hoods?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1113161307011840$
                // - A brand new world, chock full of new data to analyze!
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
