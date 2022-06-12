using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004405: Karl
/// </summary>
public class _11004405 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1113161307011827$
    // - Oh. It's you.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1113161307011828$
                // - This whole situation is unreal.
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
