using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000020: Marina
/// </summary>
public class _11000020 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407000101$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000104$
                // - I still can't believe that the road to $map:02000001$ is out. All the supplies for the empress's court have been sent along that road. Do you think anyone fell in when the ground opened up? Yeesh.
                return -1;
            case (40, 0):
                // $script:0831180407000105$
                // - The open court of the empress is just around the corner, and yet bad things are happening constantly around here. First the supply carriage was robbed, and then the earthquake happened. All I wanted was for all this to go smoothly.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
