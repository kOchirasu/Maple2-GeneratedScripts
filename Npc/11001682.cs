using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001682: Zabeth
/// </summary>
public class _11001682 : NpcScript {
    internal _11001682(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0629000607006468$ 
                // - What're you staring at? You want a piece of me?
                return true;
            case 30:
                // $script:0629000607006471$ 
                // - You got something to stay, or you just gonna stand there and stare all night? Actually, I don't care. Get outta here.
                switch (selection) {
                    // $script:0706173707006643$
                    // - How are you doing?
                    case 0:
                        Id = 40;
                        return false;
                    // $script:0708220807006669$
                    // - What do you know about the $map:52000034$?
                    case 1:
                        Id = 50;
                        return false;
                    // $script:0708220807006670$
                    // - What happened to the vagrants Blackstar took hostage?
                    case 2:
                        Id = 60;
                        return false;
                    // $script:0712221207006734$
                    // - Tell me about $npcName:11001547[gender:0]$.
                    case 3:
                        Id = 70;
                        return false;
                }
                return true;
            case 40:
                // $script:0708220807006671$ 
                // - What do you want to hear? Tales of my exploits? The names of punks I beat to a bloody pulp?
                switch (selection) {
                    // $script:0708220807006672$
                    // - How did you get the name "Zabeth?"
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0708220807006673$ 
                // - Wh-why do you want to know? Did $npcName:11001674[gender:0]$ put you up to this?
                // $script:0708220807006674$ 
                // - Ahem! Don't listen to that fool. My name is Eliza—
                // $script:0708220807006675$ 
                // - I-I mean, it's $npcName:11001682[gender:0]$! Just $npcName:11001682[gender:0]$, got it?!
                switch (selection) {
                    // $script:0708220807006676$
                    // - Your name is Eliza-what?
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:0708220807006677$ 
                // - Quit it with the stupid questions! It's none of your business!
                switch (selection) {
                    // $script:0708225907006702$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 50:
                // $script:0708220807006678$ 
                // - Is that what this place's called? I didn't know that. I don't care, neither. I just want to get back to base. I belong at $map:63000020$, watching over the fighters. This town doesn't hold a candle to the excitement of the ring.
                // $script:0706173707006644$ 
                // - That place before... You could feel the fighting spirit in the air! This place, on the other hand... Words don't do it justice.
                switch (selection) {
                    // $script:0708225907006703$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 60:
                // $script:0708220807006679$ 
                // - I got no idea who you're talking about. Ask $npcName:11001674[gender:0]$. Now, the one I'm interested in... is you. They say you're the Gray Wolf. I don't buy it, 'cause why would the Gray Wolf work with the boss? Gray Wolf or not, you could fight your way to the top of Blackstar if you wanted.
                switch (selection) {
                    // $script:0708220807006680$
                    // - My code of honor wouldn't allow that.
                    case 0:
                        Id = 61;
                        return false;
                }
                return true;
            case 61:
                // $script:0708220807006681$ 
                // - Code of honor! That's rich. Sounds like you're too much of a coward to take on Blackstar. Can't blame you, though. I wouldn't want to fight me, neither.
                switch (selection) {
                    // $script:0708220807006682$
                    // - (Raise your fists.)
                    case 0:
                        Id = 62;
                        return false;
                }
                return true;
            case 62:
                // $script:0708220807006683$ 
                // - Uh...! D-did you hear that? M-my stomach's calling. I better go home and... and turn it off...
                switch (selection) {
                    // $script:0708225907006704$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 70:
                // $script:0712221207006735$ 
                // - Yeah? What do you want to know?
                switch (selection) {
                    // $script:0712221207006736$
                    // - I want to know about $npcName:11001547[gender:0]$'s fighting style.
                    case 0:
                        Id = 71;
                        return false;
                }
                return true;
            case 71:
                // $script:0712221207006737$ 
                // - What're you asking me for? You're the one who faced him in the ring! I told you he'd take you out with a single punch, didn't I? Ha!
                switch (selection) {
                    // $script:0712221207006738$
                    // - How does $npcName:11001547[gender:0]$ train?
                    case 0:
                        Id = 72;
                        return false;
                }
                return true;
            case 72:
                // $script:0712221207006739$ 
                // - Trying to figure out how he got so strong, eh? I think he was just born strong. I hear he never slacks off on his training, but no amount of training makes you as tough as he is.
                // $script:0712221207006740$ 
                // - He's got a 30-step routine he goes through every single day. Enough to give a normal man a heart attack, they say. Some of the other lunks in the organization tried it, and they all passed out foaming at the mouth.
                switch (selection) {
                    // $script:0712221207006741$
                    // - What's the routine?
                    case 0:
                        Id = 73;
                        return false;
                }
                return true;
            case 73:
                // $script:0712221207006742$ 
                // - It's nothing special, really. 4,000 knuckle push-ups, 1,000 finger push-ups, 5,000 sit-ups, 5,000 squats, 200 laps around the track... That sort of thing.
                // $script:0712221207006743$ 
                // - He uses sandbags and chunks of meat as punching bags, and he lets others whale on him to toughen him up. There's no secret to his training. He's just that tough.
                switch (selection) {
                    // $script:0712221207006744$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
