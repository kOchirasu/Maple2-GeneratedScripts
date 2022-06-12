using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004146: Mint
/// </summary>
public class _11004146 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010563$
    // - Mm? Are you here to see little old me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010564$
                // - Hello! It's another beautiful day in Royale Park, wouldn't you say?
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
