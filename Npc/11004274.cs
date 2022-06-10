using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004274: Cheche
/// </summary>
public class _11004274 : NpcScript {
    internal _11004274(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911203207011259$ 
                // - What a wonderful, joyous day!
                return true;
            case 10:
                // $script:0911203207011260$ 
                // - What a wonderful, joyous day!
                switch (selection) {
                    // $script:0911203207011261$
                    // - What are you so happy about?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0911203207011262$ 
                // - Every day is a joy! I was sent up here because I was scared of the desert monsters, and at first, I was scared of being so high up, too... But I've adjusted!
                // $script:0911203207011263$ 
                // - I'm overjoyed to be in such a safe place. Now I have friends and don't need to be scared of any monsters!
                // $script:0913152507011309$ 
                // - Stay positive, and good fortune will follow! Never forget that, human!
                return true;
            default:
                return true;
        }
    }
}
