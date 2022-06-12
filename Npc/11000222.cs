using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000222: Patrick
/// </summary>
public class _11000222 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000970$
    // - May I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000972$
                // - I've got a daughter. She's the apple of my eye. Her name is $npcName:11000221[gender:1]$. She was the last gift my wife gave me before she passed away.
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
