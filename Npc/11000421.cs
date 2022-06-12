using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000421: Benielle
/// </summary>
public class _11000421 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001760$
    // - May I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001762$
                // - I came here with my daughter $npcName:11000420[gender:1]$ to start a new life. But if those turtles don't stop showing up, we'll have to move again.
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
