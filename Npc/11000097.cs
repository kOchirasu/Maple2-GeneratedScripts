using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000097: Solvay
/// </summary>
public class _11000097 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000381$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000382$
                // - The Barrota Trading Company is Maple World's biggest mercantile organization. Its hawkers go everywhere in the world, no matter how steep or dangerous.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
