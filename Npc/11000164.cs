using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000164: Vale
/// </summary>
public class _11000164 : NpcScript {
    internal _11000164(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000694$ 
                // - What seems to be the problem?
                return true;
            case 30:
                // $script:0831180407000697$ 
                // - Sigh... I knew this was a dangerous job, but I volunteered anyway because it pays twice as much as other jobs I've had. Maybe I shouldn't have taken it, though. I would've been safer hauling fish at the harbor.
                return true;
            case 40:
                // $script:0831180407000698$ 
                // - If not for the earthquake, the Royal Road wouldn't have been destroyed and I could've been in $map:02000001$ by now. I'd be done with my delivery, and kicking back while waiting for the court to open.
                // $script:0831180407000699$ 
                // - Actually, if the supplies for the court weren't stolen to begin with, the palace wouldn't have needed the replacements in such a hurry. This is a mess.
                return true;
            default:
                return true;
        }
    }
}
