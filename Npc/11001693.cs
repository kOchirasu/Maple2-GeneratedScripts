using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001693: Zabeth
/// </summary>
public class _11001693 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0629205207006508$
    // - If you got something to say, say it.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0629205207006510$
                // - I don't care what $npcName:11001631[gender:0]$ says. I call the shots around here, and don't you forget it.
                return 30;
            case (30, 1):
                // $script:0630212007006534$
                // - Remember, that guy's all talk and no action. I can beat him with one hand tied behind my back.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
