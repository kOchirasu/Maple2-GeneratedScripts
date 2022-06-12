using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001105: Eve
/// </summary>
public class _11001105 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0908154107003710$
    // - What brings you to me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0908154107003714$
                // - If $npcName:11000064[gender:0]$ hadn't come to Katramus to save me, I could've been here with these people for treatment.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
