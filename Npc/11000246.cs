using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000246: Beans
/// </summary>
public class _11000246 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001046$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001048$
                // - My dream is to live in a bigger and nicer house with $npcName:11000401[gender:0]$.
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
