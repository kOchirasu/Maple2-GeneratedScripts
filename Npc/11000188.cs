using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000188: Rael
/// </summary>
public class _11000188 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407000826$
    // - Cough, cough... Yes?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000828$
                // - I'm still cold... But I have to get better soon. My grandma is worried about me... Cough, cough... 
                return -1;
            case (30, 0):
                // $script:0831180407000829$
                // - I wonder what happened to my parents... Cough... I hope they're still out there...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
