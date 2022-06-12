using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004152: Tina
/// </summary>
public class _11004152 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010575$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010576$
                // - The scenery here is breathtaking, but if you want the best view in $map:02000499$, you should try hanging from $npcName:11004165$.
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
